# Test Doubles

## Stub object
> Has the same methods as the class it replaces but the implementation is very simple
> Looks good from the outside
> Contains nothing except what you put there
> Responds with fixed, pre-prepared data
> You use one when it's inconvenient to use the real collaborate object.
    - like when the real object relies on a resource that is not available on the unit test.
> Will not fail the test

## Fake object
> Unlike a stub, it has a realistic implementation with the logic and behavior of the class it replaces
> It's somewhat unusable in production but similar enought to the real class that we can use it for test purposes.


## Dummy object
> It doesn't matter what it looks like
> A dummy is not used
> It's usually None, or an empty list, etc
> You use a dummy when you're forced to pass an argument to the method or function under test, but that collaborator isn't used in the scenario you're testing.

## Spy
> Can fail the test if it's not called correctly
> Records the method calls it receivs so you can assert they were correct
> You use a spy when you want to make sure the interaction of two objects are happening correctly.

## Mock
> Can fail the test if it's not called correctly
> Knows what method calls to expect and fails the test if they are incorrect
> Expect certain method calls otherwise raise an error
> You use a mock when you want to make sure the interaction of two objects are happening correctly 
> and you want the test to fail fast, as soon as any incorrect interaction happens.
> Gives you the stack trace of where the failure actually happens

