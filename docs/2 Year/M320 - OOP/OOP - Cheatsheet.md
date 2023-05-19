This cheat sheet provides code examples for essential concepts in Java's object oriented programming. 

## Class Definitions

-   Blueprint for creating objects
-   Contains fields (data) and methods (behavior)
-   Used to create instances (objects) of the class

```java
class ClassName {
    // Fields/Instance Variables
    dataType fieldName;

    // Constructor
    ClassName(parameters) {
        // Constructor body
    }

    // Methods
    returnType methodName(parameters) {
        // Method body
    }
}
```

## Creating Objects
-   Instantiates a new object of a class
-   Allocates memory and initializes the object
-   Returns a reference to the newly created object

```java
ClassName objectName = new ClassName();
```

## Accessing

-   Allows access to fields and methods of an object
-   Dot notation: objectName.fieldName or objectName.methodName()
-   Accessed based on the reference type (compile-time type)

```java
objectName.fieldName; // Accessing instance variable
objectName.methodName(parameters); // Invoking a method
```

## Inheritance

-   Enables a class to inherit properties and methods from a parent class
-   Supports code reuse and hierarchical relationships
-   Allows overriding and extending functionality

- Extending a superclass to inherit its properties and methods, promoting code reuse and establishing a hierarchical relationship, enabling subclasses to specialize and override inherited behavior while maintaining the ability to be used as instances of their superclass. Example for dog you can create a parentclass named animal and define attributes that is general for any animal.

```java
class ChildClass extends ParentClass {
    // Additional members and methods
}
```

## Polymorphism

-   Ability of an object to take different forms (classes)
-   Enables methods to be overridden in subclasses
-   Supports dynamic method dispatch at runtime

- Utilizing polymorphic references to create code that is more flexible and modular, allowing objects of different subclasses to be treated as instances of their common superclass, facilitating dynamic method dispatch and enabling runtime determination of the specific behavior of an object.

```java
// Method overriding
@Override
returnType methodName(parameters) {
    // Method body
}
```

## Encapsulation

-   Bundles data and methods into a single unit (class)
-   Access modifiers control the visibility and accessibility of members
-   Protects data from unwanted external access

```java
private dataType fieldName; // Accessible only within the class
public dataType fieldName; // Accessible from anywhere
protected dataType fieldName; // Accessible within the class and its subclasses
```

## Abstraction

-   Hides unnecessary details and complexity
-   Provides a simplified view of objects and classes
-   Abstract classes and interfaces are used to achieve abstraction

- Creating an abstract class or interface to define a common set of methods that multiple subclasses must implement, allowing for code reuse and providing a simplified view of the objects.

```java
abstract class AbstractClass {
    // Abstract method
    abstract returnType methodName(parameters);
}
```

## Interfaces

-   Defines a contract of methods that a class must implement
-   Allows multiple inheritance of behavior
-   Encourages loose coupling and code flexibility

- Implementing an interface to ensure that a class adheres to a specific contract of methods, enabling loose coupling, flexibility, and allowing objects of different classes to be treated interchangeably based on their shared interface.

```java
interface InterfaceName {
    // Constant declarations
    dataType CONSTANT_NAME = value;

    // Abstract method declarations
    returnType methodName(parameters);
}

class ClassName implements InterfaceName {
    // Implement interface's methods
}
```

## Polymorphic References

-   Allows an object of a subclass to be referred to by a superclass reference
-   Supports code flexibility and modularity
-   Enables method overriding and dynamic method dispatch

```java
ParentClass referenceName = new ChildClass();
```

## Static Members

-   Belongs to the class rather than instances (objects)
-   Accessed using the class name
-   Shared among all instances of the class

```java
class ClassName {
    static dataType staticFieldName;
    static returnType staticMethodName(parameters) {
        // Method body
    }
}

ClassName.staticFieldName; // Accessing static field
ClassName.staticMethodName(parameters); // Invoking static method
```

## Final Keyword

-   Indicates that a variable, method, or class cannot be changed or overridden
-   Provides constants and immutable behavior
-   Used to achieve data integrity and code safety

```java
final dataType fieldName; // Cannot be modified after initialization

final void methodName() {
    // Cannot be overridden in subclasses
}
```

## Exceptions

-   Handles exceptional conditions or errors during program execution
-   Protects against unexpected behavior and allows error recovery

```java
try {
    // Code that may throw an exception
} catch (ExceptionType exceptionObject) {
    // Handling the exception
} finally {
    // Code that always executes
}
```

## Packages

-   Organizes classes and interfaces into namespaces
-   Facilitates code reusability and modular development

```java
package packageName;

import packageName.ClassName;
import packageName.*; // Import all classes in the package
```

## String Manipulation

- Provides operations for manipulating string data

```java
String str = "Hello, World!";

str.length(); // Length of the string
str.charAt(index); // Get character at a specific index
str.substring(startIndex, endIndex); // Extract substring
str.indexOf(substring); // Index of substring in the string
str.replace(oldValue, newValue); // Replace characters in the string
str.toLowerCase(); // Convert to lowercase
str.toUpperCase(); // Convert to uppercase
str.trim(); // Remove leading and trailing whitespace
```