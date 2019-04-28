# We have our generic interface "Context"
Context uses different strategies to perform tasks based on what the client invocates 
(calls).

Strategies are our toolbox: The context is the craftsman. The context calls the 
appropiate strategy based on client request.

# Steps
1. Define your Strategies, which all must have the same method signatures
2. Define a context/manager, that calls a general method which will switch to needed 
functionality because of the power of overloading! 
