# **Conclusiones**

El ejercicio de pruebas automatizadas para la API de Petstore Swagger se completó con éxito utilizando **Karate** como herramienta clave. Durante la implementación, se abarcaron aspectos esenciales del flujo de la API, con los siguientes resultados:

- Se logró automatizar de manera eficaz los escenarios más importantes: añadir una mascota, recuperarla por ID, actualizar su estado a "Sold" y realizar búsquedas por estado. Esto nos permitió verificar que los principales flujos del sistema funcionen correctamente, lo que es crucial en entornos de producción.

- La integración de **Karate** con **Maven** fue fluida y eficiente, permitiendo la ejecución de las pruebas sin complicaciones. El enfoque basado en BDD no solo facilita la lectura de los casos de prueba, sino que también asegura que sean fáciles de mantener y expandir a medida que crece el proyecto o el equipo.

- Las pruebas no solo verificaron la funcionalidad de la API, sino que también validaron de forma efectiva los estados y respuestas del sistema. Un caso destacado fue la correcta actualización del estado de la mascota a "Sold", lo que nos dio la seguridad de que los procesos internos de la API funcionan según lo esperado.

- La ejecución de las pruebas se realizó sin inconvenientes y los resultados arrojaron un funcionamiento estable de la API en cada uno de los escenarios planteados. Los mensajes de respuesta y los códigos de estado HTTP fueron validados correctamente, lo que demostró que la API responde conforme a las especificaciones esperadas.

En resumen, este proyecto no solo confirmó la estabilidad de los endpoints de la API, sino que también demostró que la estrategia de automatización utilizada es eficiente y escalable. Esto permitirá que, en el futuro, el sistema se amplíe con nuevas pruebas sin sacrificar agilidad ni calidad en el proceso.

**Atentamente,**

**SDET Alexander J.**
