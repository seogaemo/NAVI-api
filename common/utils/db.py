import psycopg2

from api.common.dto.prediction.response import PredictionResponse
from api.common.utils.config import Settings


class DB:
    def __init__(self):
        self.settings = Settings()

        self.conn = psycopg2.connect(
            dbname=self.settings.DB_NAME,
            user=self.settings.DB_USER,
            password=self.settings.DB_PASSWORD,
            host=self.settings.DB_HOST,
            port=self.settings.DB_PORT,
        )

        self.cur = self.conn.cursor()

        if self.checkPointTableIsExist() is False:
            raise Exception("Table 'road_data' does not exist")

        if self.checkPredctionTableIsExist() is False:
            self.createPredictionTable()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def checkPointTableIsExist(self):
        query = """
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_name = 'road_data'
        )
        """

        self.cur.execute(query)
        return self.cur.fetchone()[0]

    def checkPredctionTableIsExist(self):
        query = """
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_name = 'prediction_data'
        )
        """

        self.cur.execute(query)
        return self.cur.fetchone()[0]

    def createPredictionTable(self):
        query = """
        CREATE TABLE prediction_data (
            point_id TEXT PRIMARY KEY,
            predictions JSONB NOT NULL
        )
        """

        self.cur.execute(query)
        self.conn.commit()

    def getNearestLocations(self, lat: float, lng: float, limit: int = 3):
        # 10미터 제한
        query = """
        SELECT *
        FROM (
            SELECT id, lat, lng, ele, time, duration, speed, video, image,
                (6371 * acos(cos(radians(%s)) * cos(radians(lat)) * cos(radians(lng) - radians(%s)) + sin(radians(%s)) * sin(radians(lat)))) AS distance 
            FROM road_data 
        ) AS subquery
        WHERE distance <= 0.01 AND image = '1'
        ORDER BY distance
        LIMIT %s
        """

        self.cur.execute(query, (lat, lng, lat, limit))
        rows = self.cur.fetchall()

        if len(rows) == 0:
            return None

        return rows

    def getPrediction(self, pointId: str) -> PredictionResponse | None:
        query = """
        SELECT predictions
        FROM prediction_data
        WHERE point_id = %s
        """

        self.cur.execute(query, (pointId,))
        row = self.cur.fetchone()

        if row is None:
            return None

        return row[0]

    def savePrediction(self, pointId: str, predictions: PredictionResponse):
        query = """
        INSERT INTO prediction_data (point_id, predictions)
        VALUES (%s, %s)
        ON CONFLICT (point_id) DO UPDATE
        SET predictions = %s
        """

        self.cur.execute(
            query,
            (
                pointId,
                predictions.model_dump_json(),
                predictions.model_dump_json(),
            ),
        )
        self.conn.commit()
