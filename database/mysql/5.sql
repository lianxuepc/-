use demo ;
create table cc (
	cc1 varchar(20) primary key not null,
    cc2 int not null,
    cc3 dec(10,2) ,
    cc4 varchar(60)
);

insert into demo.cc(cc1,cc2,cc3,cc4)
values
('赵一','20','580.00','重邮宿舍12-3-5'),
('钱二','19','540.00','南福苑5-2-9'),
('孙三','21','555.50','学生新区21-5-15'),
('李四','22','480.00','重邮宿舍8-2-22'),
('周五','20','495.50','学生新区23-4-8'),
('吴六','19','435.00','南福苑2-5-12');

set sql_safe_updates=0;
update demo.cc set cc3=cc3+5 where cc2<=20;

delete from demo.cc
where cc2>=20 and cc3>=500;