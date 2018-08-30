
from flask import Flask, jsonify, request
import pymysql
import sys

REGION = 'us-east-2'

rds_host = 'xbias-backend.cytnlddqky1c.us-east-2.rds.amazonaws.com'
username = 'xBias_master'
password = 'Kr19972=14'
db_name = 'xbias_backend'

ret_json_list=[]
conn = pymysql.connect(rds_host, user = username, passwd = password, db= db_name, connect_timeout = 5)
with conn.cursor() as cur:
	cur.execute("""SELECT * FROM article_entry_logger""")
	result = cur.fetchall()
	cur.close()
	i=1
	for row in result:
		print(row)
		temp_json_entry={'entry_{n}'.format(n=i): {
			'article_entry_id': row[0],
			'article_name': row[1],
			'article_link': row[2],
			'articles_news_org': row[3],
			'article_bias_score': row[4],
			'device_id': row[5],
			'device_interface': row[6],
			'click_timestamp': row[7]
			}
		}
		print(temp_json_entry)
		ret_json_list.append(temp_json_entry)
		i+=1