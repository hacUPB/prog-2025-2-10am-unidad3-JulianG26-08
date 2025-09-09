|Nombre de la variable|	Tipo de dato|	Tipo de variable|	Descripción|
|-------------------  |-------------|-------------------|--------------|
|T_min	              |Real	        |Entrada            |	Límite inferior permitido de temperatura.|
|T_max                |Real         |Entrada            |	Límite superior permitido de temperatura.|
|k	                  |Real	        |Entrada            |	Constante de enfriamiento/calentamiento.
|intervalo            |Entero       |Entrada            |	Tiempo entre monitoreos de temperatura (en minutos).|
|tiempo_vuelo	      |Entero       |Entrada	        |Duración total del vuelo.|
|Te                   |Real	        |Entrada	        |Temperatura del entorno.|
|T_actual             |Real	        |Control	        |Temperatura actual de una llanta en un momento dado.|
|tiempo_actual	      |Entero	    |Control	        |Tiempo transcurrido desde el despegue.|
|dT_dt	              |Real	        |Control	        |Tasa de cambio de temperatura calculada.|
|T_nueva	          |Real	        |Control	        |Temperatura después de aplicar corrección.
|tiempo_estabilizacion|Entero	    |Control	        |Tiempo antes del aterrizaje en el que la temperatura debe estar estable.|
|tiempo_inicio_estabilizacion|Entero|Control	        |Tiempo donde inicia la fase crítica antes del aterrizaje.|
|mostrarAlerta(mensaje)|Función / salida|Salida	        |Función que alerta en cabina si la temperatura no está en el rango esperado.|
|RegistrarTemperatura(t, T)|Función / salida|Salida	    |Función que guarda las temperaturas monitoreadas.|
|corregirTemperatura()|Función / salida|Salida	        |Acción correctiva ejecutada para ajustar la temperatura.|