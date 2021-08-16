# Test Doubles

## Stub object
> Has the same methods as the class it replaces but the implementation is very simple
> Looks good from the outside
> Contains nothing except what you put there
> You use one when it's inconvenient to use the real collaborate object.
    - like when the real object relies on a resource that is not available on the unit test.


## Fake object
> Unlike a stub, it has a realistic implementation with the logic and behavior of the class it replaces
> It's somewhat unusable in production but similar enought to the real class that we can use it for test purposes.