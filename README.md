# ccde_order_api
CCDE ORDER API

###构建（Build）说明
####构建数据库镜像
```
cd db
docker build -t="lennyleng/ccde_order_db" .
```
####构建API镜像
```
cd api
docker build -t="lennyleng/ccde_order_api" .
```
