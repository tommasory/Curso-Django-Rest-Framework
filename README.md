# Curso Django Rest Framework | Cero a Experto

## Vistas De Django rest framework

### _APIVIEW_

- Mas control sobre la logica
- Bueno para logica compleja
- Llamar otras APIS
- Trabajar con archivos locales

**Que es ?**

- Usa metodos HTTP estandadr
- get()
- post()
- ...

**Cuando Usar APIVIEW**

- Si necesitas control de la logica
- Proceso de archivos y renderizar respuestas sincronizada
- Llamado a otras APIS / Servicios
- Acceso a archivos locales o cualquier tipo de datos

### _ViewSets_

**Usa funciones de operaciones de modelo**

- **list()** enlista objetos
- **create()** crea objetos
- **retrieve()** obtiene objeto especifico
- **update()** actualiza un objeto
- **partial_update()** actualización parcial
- **destroy()** elimina un objeto

**¿Que son los ViewSets?**

- Se encarga de la logica comun
- Bueno para operaciones estandar de BD
- Forma mas rapida de hacer interfaz con BD

**¿Cuando usuamos ViewSets?**

- CRUD simple
- API simple
- Poca personalización de logica
- Trabaja con estructuras de datos normales


## Permisos de Usuario
**Muy importante:** Está seccion es de gran importancia porque lo que hicimos fue
colocarle seguridad al APIViewSet de perfiles, porque si no eres la persona dueña
del perfil no vas a poder editar este. esto se logro creando la clase permissions.py
en la cual si indica que si no eres dueño de ese perfil y ademas no tienes el token de
autorizacion no vas a poder editar el perfil.