- If there is an output like this in your message

`https://stackoverflow.com/questions/25745053/about-char-b-prefix-in-python3-4-1-client-connect-to-redis`

```
MY HANDLER:  b'1'
```
- Note the `b`
- This can be fixed by decoding redis message properly
```
r = redis.StrictRedis(host="localhost", port=6379, charset="utf-8", decode_responses=True)
```