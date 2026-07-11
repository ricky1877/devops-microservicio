# devops-microservicio

Este proyecto implementa una API FastAPI con automatización DevOps, contenedorización y despliegue continuo.

## Estrategia de branching

- main: rama principal y de producción.
- develop: rama de integración para nuevas funcionalidades.
- feature/*: ramas temporales para nuevas características.
- hotfix/*: ramas temporales para correcciones urgentes.

### Flujo de trabajo

1. Se crean ramas feature/* desde develop para nuevas funcionalidades.
2. Se integran mediante pull requests hacia develop.
3. Cuando el cambio está listo para producción, se hace merge desde develop hacia main.
4. Los hotfix/* se crean desde main y se integran mediante pull request.

## CI/CD

- GitHub Actions ejecuta pruebas en cada push a develop y en pull requests hacia main.
- El pipeline construye la imagen Docker, ejecuta pruebas dentro del contenedor y publica la imagen si las pruebas pasan.
- Se integra SonarQube y Snyk cuando los secretos correspondientes están configurados.

## Despliegue

- Los manifiestos de Kubernetes se encuentran en kubernetes/.
- La configuración de Istio se encuentra en istio/.
- El despliegue se activa para pushes a main cuando existe configuración de Kubernetes.

## Requisitos de seguridad

- Se recomienda proteger main con revisiones obligatorias y aprobaciones.
- Dependabot está habilitado para monitorear dependencias.

## Hotfix

- Se corrigió la documentación del proyecto para la entrega final.
