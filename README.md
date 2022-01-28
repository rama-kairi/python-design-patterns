# Design Patterns in Python

## Creational Patterns

Creational patterns are ones that create objects, rather than having to instantiate objects directly. This gives the program more flexibility in deciding which objects need to be created for a given case.

- *Abstract factory* -  groups object factories that have a common theme.
- *Builder* -  builds complex objects step by step.
- *Factory method* -  creates objects without specifying their concrete class.
- *Prototype* -  creates objects by copying existing ones.
- *Singleton* -  creates only one object and returns a reference to it.

## Structural Patterns

These concern class and object composition. They use inheritance to compose interfaces and define ways to compose objects to obtain new functionality.

- *Adapter* -  adapts an object to a new interface.
- *Bridge* -  connects classes in different abstraction layers.
- *Composite* -  combines objects into tree structures to represent part-whole hierarchies.
- *Decorator* -  adds new functionality to an object dynamically.
- *Facade* -  provides a unified interface to a set of interfaces in a subsystem.
- *Flyweight* -  minimizes memory usage by sharing as much as possible with other similar objects.
- *Proxy* -  provides a surrogate or placeholder for another object to control access.

## Behavioral Patterns

Most of these design patterns are specifically concerned with communication between objects.

- *Chain of responsibility* -  allows a series of linked objects to handle a request, one at a time, passing the request along from object to object until it reaches the end.
- *Command* -  encapsulates a request as an object, thereby letting you parameterize other objects with different requests, queue or log requests, and support undoable operations.
- *Interpreter* -  provides a way to implement language-specific functions.
- *Iterator* -  provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
- *Mediator* -  provides a way to decouple components that interact with each other.
- *Memento* -  provides a way to save and restore the state of an object without breaking its encapsulation.
- *Observer* -  allows an object to notify its observers when its state changes.
- *State* -  allows an object to alter its behavior when its internal state changes.
- *Strategy* -  allows the behavior of an object to be selected at runtime.
- *Template* -  provides a way to define the skeleton of an algorithm in an operation, deferring some steps to subclasses.
- *Visitor* -  provides a way to apply operations to different types of objects without having to change their classes.


## SOLID Principles