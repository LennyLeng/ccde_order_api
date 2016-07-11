/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     2016/7/10 10:05:25                           */
/*==============================================================*/


/*==============================================================*/
/* Table: orders                                                */
/*==============================================================*/
create table orders (
   id                   SERIAL               not null,
   proposer_name        VARCHAR(128)         null,
   proposer_work_phone  VARCHAR(128)         null,
   proposer_private_phone VARCHAR(128)         null,
   proposer_vdi_login_name VARCHAR(128)         null,
   proposer_mail_login_name VARCHAR(128)         null,
   proposer_department  VARCHAR(128)         null,
   proposer_post        VARCHAR(128)         null,
   proposer_room_num    VARCHAR(128)         null,
   service_type         VARCHAR(128)         null,
   order_type           VARCHAR(128)         null,
   order_content        TEXT                 null,
   recv_unit            VARCHAR(128)         null,
   recv_operator_name   VARCHAR(128)         null,
   begin_time           TIMESTAMP            null,
   end_time             TIMESTAMP            null,
   deal_content         TEXT                 null,
   cost_time            INTERVAL             null,
   constraint PK_ORDERS primary key (id)
);

