## manual tests


* add repo
```
curl -d '{"name":"bitnami", "url":"https://charts.bitnami.com/bitnami"}' -H "Content-Type: application/json" -X POST http://localhost:5000/repo/add | jq
```

* remove repo
```
curl -d '{"name":"bitnami"}' -H "Content-Type: application/json" -X POST http://localhost:5000/repo/remove | jq
```

* install release from chart
```
curl -d '{"name":"redis-local", "chart_name":"bitnami/redis"}' -H "Content-Type: application/json" -X POST http://localhost:5000/chart/install | jq
```

* upgrade release from chart
```
curl -d '{"name":"redis-local", "chart_name":"bitnami/redis"}' -H "Content-Type: application/json" -X POST http://localhost:5000/chart/upgrade | jq
```

* unintsall release
```
curl -d '{"name":"redis-local"}' -H "Content-Type: application/json" -X POST http://localhost:5000/chart/uninstall | jq
```

* rollback release
```
curl -d '{"name":"redis-local"}' -H "Content-Type: application/json" -X POST http://localhost:5000/chart/rollback | jq
```

### sample cmd

add_cmd = "helm repo add bitnami https://charts.bitnami.com/bitnami"
install_cmd = "helm install redis-local bitnami/redis"
upgrade_cmd = "helm upgrade redis-local bitnami/redis"
uninstall_cmd = "helm uninstall redis-local"
rollback_cmd = "helm rollback redis-local"
