DROP TABLE IF EXISTS staff;
CREATE TABLE staff (
  sid varchar(255) NOT NULL,
  sname varchar(255) NOT NULL,
  ssex varchar(255) DEFAULT NULL,
  stime date DEFAULT NULL,
  susername varchar(255) NOT NULL UNIQUE,
  spassword varchar(255) NOT NULL,
  srole varchar(255) NOT NULL,
  sidcard varchar(255) NOT NULL,
  sphone varchar(255) DEFAULT NULL,
  PRIMARY KEY (sid)
);
INSERT INTO staff VALUES ('1','张三','男','2019-12-23','zs123','123456','1','310572199012233421','13977766253'),('2','李四','女','2019-12-06','ls123','123456','2','329123199102021234','13823209876'),('3','张萍','女','2019-12-26','zp123','123456','1','332987199812262512','13782765657'),('4','赵六','女','2010-01-01','zl123','123456','1','332987199811164512','13888909890'),('5','王五','男','2020-01-01','wu123','123456','2','332987199812264512','13988767890'),('6','黄让','男','2020-01-01','hr123','123456','2','332987199811263333','13962334343'),('7','黄小平','女','2019-12-04','hxp123','123456','1','332987199811262222','13962334222'),('8','阿斯顿','男','2019-12-02','asd123','123456','1','332987199810102222','13962334333');


DROP TABLE IF EXISTS room;
CREATE TABLE room (
  rid varchar(255) NOT NULL,
  rtype varchar(255) NOT NULL,
  rstorey varchar(255) NOT NULL,
  rprice varchar(255) NOT NULL,
  rdesc varchar(255) DEFAULT NULL,
  rpic int DEFAULT NULL,
  PRIMARY KEY (rid),
--   todo
--      建立索引
);
INSERT INTO room VALUES ('201','标准间（单人）','2','208','电视故障','D:/pictures/ss.jpg'),('203','标准间（单人）','2','208','无','D:/pictures/ss.jpg'),('205','标准间（双人）','2','268','没事','D:/pictures/sd.jpg'),('207','标准间（双人）','2','268','采光好','D:/pictures/sd.jpg'),('301','标准间（单人）','3','208','采光好','D:/pictures/ss.jpg'),('303','大床房','3','258','无','D:/pictures/b.jpg'),('305','大床房','3','258','设施新','D:/pictures/b.jpg'),('307','标准间（单人）','3','208','设施新','D:/pictures/ss.jpg'),('308','总统套房','3','688','古典','D:/pictures/pr1.jpg'),('402','标准间（双人）','4','268','空调故障','D:/pictures/sd.jpg'),('404','总统套房','4','588','好评率高','D:/pictures/pr1.jpg'),('406','总统套房','4','588','好评率高','D:/pictures/pr2.jpg'),('410','标准间（单人）','4','232','新房','D:/pictures/ss.jpg');


DROP TABLE IF EXISTS team;
CREATE TABLE team (
  tname varchar(255)  NOT NULL ,
  ttid varchar(255) PRIMARY KEY,
  tphone varchar(255) DEFAULT NULL,
  check_in_sid varchar(255) DEFAULT NULL,
  accomodation_times int DEFAULT NULL,
  register_time timestamp DEFAULT NULL,
  FOREIGN KEY (check_in_sid) REFERENCES staff (sid)
);
INSERT INTO team VALUES ('hit','1','13896534534','1',2,'2020-01-06 00:50:46'),('zkl','11','13976523423','6',0,'2020-01-04 09:10:02'),('哈工大','16','13987667890','3',0,'2020-01-04 09:06:55'),('哈工大','30','13898700998','1',5,'2020-01-05 11:09:25'),('先行创业者社团','32','13962463676','2',0,'2020-01-04 09:06:37'),('腾讯','43','13829833333','1',3,'2020-01-04 11:55:01'),('家家悦','55','13678998789','2',0,'2020-01-05 06:41:05'),('合唱团','7','17878989098','6',1,'2020-01-04 09:25:37'),('alibaba','8','18978978909','4',0,'2020-01-04 09:07:48');


DROP TABLE IF EXISTS client;
CREATE TABLE client (
  cname varchar(255) NOT NULL,
  cid varchar(255) NOT NULL,
  cphone varchar(255) DEFAULT NULL,
  cage varchar(255) NOT NULL,
  csex varchar(255) DEFAULT NULL,
  register_sid varchar(255) DEFAULT NULL,
  accomodation_times int DEFAULT NULL,
  register_time timestamp ,
  PRIMARY KEY (cid),

  FOREIGN KEY (register_sid) REFERENCES staff (sid)
);
INSERT INTO client VALUES ('吴超梦','130898199212233434','13898322223','28','女','4',1,'2020-01-04 10:48:42'),('黄荣','131989238123991309','13123323212','52','男','7',1,'2020-01-04 09:24:48'),('王潇','189322199312262232','13098722343','27','男','4',1,'2020-01-06 00:17:20'),('柯镇恶','289193212393128999','13310913888','50','男','6',0,'2020-01-04 09:16:01'),('段深','290389199412280303','13898767890','26','男','5',0,'2020-01-04 09:15:32'),('黄晓让','320198199812243456','13789098789','21','女','5',3,'2020-01-04 10:06:33'),('赵超','320222199102036712','13821322312','23','男','8',2,'2020-01-04 09:24:42'),('赵重样','320678199012243333','13765434212','30','男','2',0,'2020-01-04 09:12:44'),('黄穰','320876196510200099','13876534543','55','女','1',0,'2020-01-04 09:12:26'),('黄晓让','320897189722334567','13987667890','30','男','2',1,'2020-01-04 10:09:29'),('西羊羊','320987199012234444','19876556789','30','女','3',3,'2020-01-04 09:24:50');


DROP TABLE IF EXISTS booking_client;
CREATE TABLE booking_client (
  cid varchar(255) NOT NULL,
  rid varchar(255) NOT NULL,
  start_time date DEFAULT NULL,
  end_time date DEFAULT NULL,
  booking_time timestamp ,
  remark varchar(255) DEFAULT NULL,
  PRIMARY KEY (cid,rid),

  FOREIGN KEY (cid) REFERENCES client (cid),
  FOREIGN KEY (rid) REFERENCES room (rid)
);
INSERT INTO booking_client VALUES ('131989238123991309','203','2020-01-06','2020-01-08','2020-01-06 00:49:02','不错');


DROP TABLE IF EXISTS booking_team;
CREATE TABLE booking_team (
  ttid varchar(255) NOT NULL,
  rid varchar(255) NOT NULL,
  start_time date DEFAULT NULL,
  end_time date DEFAULT NULL,
  booking_time timestamp ,
  remark varchar(255) DEFAULT NULL,
  PRIMARY KEY (ttid,rid),
  FOREIGN KEY (ttid) REFERENCES team (ttid),
  FOREIGN KEY (rid) REFERENCES room (rid)
);
INSERT INTO booking_team VALUES ('55','303','2020-01-06','2020-01-10','2020-01-06 00:52:27','新客户'),('55','305','2020-01-06','2020-01-10','2020-01-06 00:52:23','新客户'),('7','301','2020-01-10','2020-01-15','2020-01-04 09:19:22','可能晚一些'),('7','303','2020-01-10','2020-01-15','2020-01-04 09:19:36',NULL);
