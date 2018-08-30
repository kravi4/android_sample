from flask import Flask, jsonify, request
import pymysql
import sys

REGION = 'us-east-2'

rds_host = 'xbias-backend.cytnlddqky1c.us-east-2.rds.amazonaws.com'
username = 'xBias_master'
password = 'Kr19972=14'
db_name = 'xbias_backend'

conn = pymysql.connect(rds_host, user = username, passwd = password, db= db_name, connect_timeout = 5)
with conn.cursor() as cur:
	cur.execute("""CREATE TABLE IF NOT EXISTS article_table (article_hash_id VARCHAR(255), source_id VARCHAR(255), source_name VARCHAR(255), author VARCHAR(255), title VARCHAR(2000), description VARCHAR(10000), url VARCHAR(100000), image_url VARCHAR(1000000), publish_timestamp VARCHAR(255),  article_bias_score INT);""")
	cur.execute("""SELECT title FROM article_table""")
	result = cur.fetchall()
	final_results=[]
	for i in range(len(result)):
		if result[i][0] not in final_results:
			final_results.append(result[i][0])
		else:
			print(result[i][0])
	print(len(final_results))
	cur.close()