import pymysql
import ast


class DB_Controller():
    def __init__(self):
        self.host = '113.198.236.131'
        self.port = 10306
        self.user = 'lab919'
        self.passwd = 'software'
        self.db = 'TSMS'
        self.charset = 'utf8mb4'
        self.setting_json = {}


    # setting 테이블의 모든 행을 읽어서 json으로 변환하여 리턴해주는 함수
    def get_setting(self):

        node_id_list = ['stair1','901','902','903','904','905','906','907','908','toilet','stair2','910','911','912','stair3','913','914','915','916','917','918','919','920','stair1','901','902','903','904','905','906','907','908','toilet','stair2','910','911','912','stair3','913','914','915','916','917','918','919','920','stair1','901','902','903','904','905','906','907','908','toilet','stair2','910','911','912','stair3','913','914','915','916','917','918','919','920'] #~23센서 값
        DB_name = ['flame','flame','flame','flame','flame','flame','flame','flame','flame','flame','flame','flame','flame','flame','flame','flame','flame','flame','flame','flame','flame','flame','flame','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','temperature','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity','humidity']

        db = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,
                             charset='utf8', autocommit=True)
        cursor = db.cursor()

        for i in range(len(node_id_list)):
            sql = "SELECT value  from "+str(DB_name[i])+" where node_id=" + "'" +  str(node_id_list[i]) + "'" + " order by time_stamp desc"
            cursor.execute(sql)
            data = cursor.fetchone()
            # print(data)
            query_to_dict = ast.literal_eval("{'"+str(node_id_list[i])+"_"+str(DB_name[i])+"':"+str(data[0])+"}")
            print(query_to_dict)
            self.setting_json.update(query_to_dict)
        #
        #
        # while True:
        #     data = cursor.fetchone()
        #     if not data:
        #         break
        #     query_to_dict = ast.literal_eval("{'" + data[1] + "':" + str(data[2]) + "}")
        #     print(query_to_dict+"Gggggg")
        #     self.setting_json.update(query_to_dict)
        db.close()
        return self.setting_json

    def set_setting(self, node_id, value):
        db = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db, charset='utf8', autocommit=True)
        cursor = db.cursor()
        sql = "UPDATE temperature SET value = " + str(value) + " WHERE node_id = '" + str(node_id) + "';"
        print(sql)
        cursor.execute(sql)
        db.close()
        return 1


if __name__ == '__main__':
    a = DB_Controller()
    print(a.get_setting())



