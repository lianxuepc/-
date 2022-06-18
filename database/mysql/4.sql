use demo;
create table aa
(
	aa1 varchar(20) primary key not null,
    aa2 int,
    aa3 dec(10,2)
    );
create table bb
	(bb1 varchar(30) primary key not null,
    bb2 int,
    bb3 dec(6,2)
    );
drop table aa;

alter table bb 
add (bb4 varchar(40));

create view vb1 as select bb1 from bb ;
create view vb4 as select bb4 from bb ;

drop view vb1,vb4;

create index indexbb on bb(bb3);
drop index indexbb;
