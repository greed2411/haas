# haas

<p align="center">
  <br>
  <img src="https://i.postimg.cc/pTW37wrQ/hare.jpg" height=352 width=282 />
  <br>
  <em>Haas is a German surname derived from the name of the mammal hare.</em><br>
  <em>image belongs to Lily Seika Jones from designyoutrust.com</em>
  <br>
  <br>
</p>


> haas stands for Helm-as-a-Service

kubernetes is nice.
helm is nice.
argoproj is nice. 

But I thought it'd be simple to have a REST API which does what [helm](https://helm.sh/) does via CLI.
It is just a [FastAPI](https://fastapi.tiangolo.com/) server wrapping a helm3 binary.

## API Documentation and examples,

## add repo


| Name | HTTP Action | Description | Parameters type|
| ---  | ----        | ----        | ---           |
| /repo/add| POST | add a chart repository | json |

### Paramaters

| Name | Description | Optional    |
| ---  | ----        | ----        |
|name| name of the chart repository to be stored locally| required|
|url| url to the chart repository/museum| required|


**example usage:**


```bash
curl -d '{"name":"bitnami", "url":"https://charts.bitnami.com/bitnami"}' -H "Content-Type: application/json" -X POST http://localhost:5000/repo/add | jq
```

**CLI equivalent:**
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
```

## remove repo



| Name | HTTP Action | Description | Parameters type|
| ---  | ----        | ----        | ---           |
| /repo/remove| POST | remove a chart repository | json |

### Paramaters

| Name | Description | Optional    |
| ---  | ----        | ----        |
|name| name of the chart repository| required|


**example usage:**


```bash
curl -d '{"name":"bitnami"}' -H "Content-Type: application/json" -X POST http://localhost:5000/repo/remove | jq
```

**CLI equivalent:**
```bash
helm repo remove bitnami
```



## install release from chart

| Name | HTTP Action | Description | Parameters type|
| ---  | ----        | ----        | ---           |
| /chart/install| POST | install a chart archive to create a release| json |

### Paramaters

| Name | Description | Optional    |
| ---  | ----        | ----        |
|name| name of the release | required|
|chart_name| name of the chart from repository | required|


**example usage:**


```bash
curl -d '{"name":"redis-local", "chart_name":"bitnami/redis"}' -H "Content-Type: application/json" -X POST http://localhost:5000/chart/install | jq
```

**CLI equivalent:**
```bash
helm install redis-local bitnami/redis
```

## upgrade release from chart

| Name | HTTP Action | Description | Parameters type|
| ---  | ----        | ----        | ---           |
| /chart/upgrade| POST | upgrade release to a new version of chart | json |

### Paramaters

| Name | Description | Optional    |
| ---  | ----        | ----        |
|name| name of the release | required|
|chart_name| name of the chart from repository | required|


**example usage:**

```bash
curl -d '{"name":"redis-local", "chart_name":"bitnami/redis"}' -H "Content-Type: application/json" -X POST http://localhost:5000/chart/upgrade | jq
```

**CLI equivalent:**
```bash
helm upgrade redis-local bitnami/redis
```

## unintsall release

| Name | HTTP Action | Description | Parameters type|
| ---  | ----        | ----        | ---           |
| /chart/uninstall| POST | uninstall a release | json |

### Paramaters

| Name | Description | Optional    |
| ---  | ----        | ----        |
|name| name of the release | required|


**example usage:**

```bash
curl -d '{"name":"redis-local"}' -H "Content-Type: application/json" -X POST http://localhost:5000/chart/uninstall | jq
```

**CLI equivalent:**
```bash
helm uninstall redis-local
```

## rollback release

| Name | HTTP Action | Description | Parameters type|
| ---  | ----        | ----        | ---           |
| /chart/rollback| POST | rollback the release to the previous version | json |

### Paramaters

| Name | Description | Optional    |
| ---  | ----        | ----        |
|name| name of the release | required|


**example usage:**

```bash
curl -d '{"name":"redis-local"}' -H "Content-Type: application/json" -X POST http://localhost:5000/chart/rollback | jq
```


**CLI equivalent:**
```bash
helm rollback redis-local
```

## About this project

This project is inspired mostly from other repositories which solve the same problem (of deploying pods using helm but over REST):
* [microsoft/helm-web-api](https://github.com/microsoft/helm-web-api)
* [opskumu/helm-wrapper](https://github.com/opskumu/helm-wrapper)

## TODO

- [ ] Dockerfile and image for this service
- [ ] setup kubectl in Dockerfile
- [ ] setup k8s cluster pointing via kubeconfig in Dockerfile
- [ ] setup helm in Dockerfile
- [ ] ingress via nginx to open up the deployments to public
- [ ] soft restart rollout gracefully for stateless deployments
- [ ] namespace support
- [ ] other ways of installing charts (from index.yaml url)
- [ ] install/upgrade overides with --values flag and json parameter
- [ ] maybe helmfile support too in the future.
