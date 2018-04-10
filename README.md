DriveWealth
==================

Integración Python con la API de DriveWealth.


Uso
===

 * Obtener una session.
```
>> import drivewealth
>> dw = drivewealth.Api(username='username', password='password')
>> print dw
```

 * Obtener la cuenta asociada a la session.
```
>> import drivewealth
>> dw = drivewealth.Api(username='username', password='password')
>> dw.accounts
```

 * Obtener data de un usuario en especifico.
    * @Params:
        - user_id
```
>> import drivewealth
>> dw = drivewealth.Api(username='username', password='password')
>> dw.get_user('user_id')
```

 * Obtener el listado de todos los instrumentos disponibles.
```
>> import drivewealth
>> dw = drivewealth.Api(username='username', password='password')
>> dw.get_instruments()
```

 * Obtener un instrumento en especifico.
    * @Params:
        - instrument_id
```
>> import drivewealth
>> dw = drivewealth.Api(username='username', password='password')
>> dw.get_instrument('instrument_id')
```

 * Buscar un instrumento.
    * @Params:
        - symbol
        - name
        - tag
```
>> import drivewealth
>> dw = drivewealth.Api(username='username', password='password')
>> dw.search_instruments(symbol='symbol', name='name', tag='tag')
```
