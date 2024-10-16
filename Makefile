superset:
	docker compose exec -it superset superset fab create-admin \
               --username admin \
               --firstname admin \
               --lastname admin \
               --email admin@admin.com \
               --password admin; \
	docker compose exec -it superset superset db upgrade; \
	docker compose exec -it superset superset load_examples; \
	docker compose exec -it superset superset init;
