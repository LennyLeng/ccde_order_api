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

###运行（Run）说明
####常规运行说明
```
docker run --name ccde_order_db -e POSTGRES_PASSWORD=Order.ccde.cnpc -e POSTGRES_DB=ccde_order_db -d -p 5432:5432 lennyleng/ccde_order_db
docker run --name ccde_order_api -d -p 80:80 --link ccde_order_db:ccde_order_db -e DB_HOST=ccde_order_db -e DB_LOGIN_NAME=postgres -e DB_LOGIN_PASS=Order.ccde.cnpc -e DB_NAME=ccde_order_db -e CPK_TOPLIMIT_SEC=7200 --name "ccde_order_api" lennyleng/ccde_order_api
```
####Docker-Compose运行说明
