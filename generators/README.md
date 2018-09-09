- A generator is a function that returns an object (iterator) which we can iterate over one value at a time

```
Think of it like this, with a generator and no send, it's a one way street

==========       yield      ========
Generator |   ------------> | User |
==========                  ========
But with send, it becomes a two way street

==========       yield       ========
Generator |   ------------>  | User |
==========    <------------  ========
                  send
```