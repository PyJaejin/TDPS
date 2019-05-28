import pymysql
import ast


class DB_Controller():
    def __init__(self):
        self.host = '113.198.236.131'
        self.port = 10306
        self.user = 'lab919'
        self.passwd = 'software'
        self.db = 'TSMS'
        self.setting_json = {}


    # setting 테이블의 모든 행을 읽어서 json으로 변환하여 리턴해주는 함수
    def get_setting(self):

        node_id_list = [911,912] #~23센서 값

        db = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,
                             charset='utf8', autocommit=True)
        cursor = db.cursor()

        for i in range(len(node_id_list)):
            sql = "SELECT *  from sensor where node_id=" + str(node_id_list[i]) + " order by time_stamp desc"
            cursor.execute(sql)
            data = cursor.fetchone()
            print(data)
            query_to_dict = ast.literal_eval("{'"+str(node_id_list[i])+"_temperature':"+str(data[2])+",'"+str(node_id_list[i])+"_humidity':"+str(data[3])+"}")
            print(query_to_dict)
            self.setting_json.update(query_to_dict)


        while True:
            data = cursor.fetchone()
            if not data:
                break
            query_to_dict = ast.literal_eval("{'" + data[1] + "':" + str(data[2]) + "}")
            self.setting_json.update(query_to_dict)
        db.close()
        return self.setting_json


if __name__ == '__main__':
    a = DB_Controller()
    print(a.get_setting())



