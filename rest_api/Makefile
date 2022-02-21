run_con_env_django:
	docker run -d -p 8000:8000 -e PORT=8000 -v my_vol:/app2/data --rm --name smart_con --network my_network smart_im
run_con_django:
	docker run -d -p 8000:8000 -v my_vol:/app2/data --rm --name smart_con --network my_network smart_im
run_con_env-file_django:
	docker run -d -p 8000:8000 --env-file ./env -v my_vol:/app2/data --rm --name smart_con --network my_network smart_im
run_im:
	docker build -t smart_im .
create_network:
	docker network create --driver=bridge my_network
run_con_db:
	docker run -d -p 5432:5432 postgres --network my_network

