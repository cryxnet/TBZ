## Introduction

Testing is an integral part of software development that ensures the reliability and correctness of your code. In Java, JUnit is a widely used testing framework that provides a simple and efficient way to write and execute tests.

## Getting Started

### Step 1: Set Up Your Project

Make sure you have a Java project set up. You can use a build tool like Maven or Gradle to manage dependencies and build your project.

### Step 2: Add JUnit Dependency

Add the JUnit dependency to your project. For Maven, add the following to your `pom.xml` file:

```xml
<dependencies>
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.12</version> <!-- or the latest version -->
        <scope>test</scope>
    </dependency>
</dependencies>
```

For Gradle, add the following to your `build.gradle` file:

```gradle
testImplementation 'junit:junit:4.12' // or the latest version
```

### Step 3: Write Your First Test

Create a new Java class for your test. The class name should end with `Test`. For example, if you are testing a class named `Calculator`, your test class could be named `CalculatorTest`.

```java
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class CalculatorTest {

    @Test
    public void testAddition() {
        Calculator calculator = new Calculator();
        int result = calculator.add(2, 3);
        assertEquals(5, result);
    }
}
```

### Step 4: Run Your Tests

Use your IDE or build tool to run your tests. JUnit will execute the tests and provide a report on the success or failure of each test.

## Writing Tests

### Annotations

- `@Test`: Denotes a test method.
- `@Before`: Executed before each test method. Used for setup.
- `@After`: Executed after each test method. Used for cleanup.
- `@BeforeClass`: Executed once before any test methods. Used for setup.
- `@AfterClass`: Executed once after all test methods. Used for cleanup.

### Assertions

JUnit provides various assertion methods for validating expected results.

- `assertEquals(expected, actual)`: Asserts that two values are equal.
- `assertTrue(condition)`: Asserts that a condition is true.
- `assertFalse(condition)`: Asserts that a condition is false.
- `assertNull(object)`: Asserts that an object is null.
- `assertNotNull(object)`: Asserts that an object is not null.

For more information, refer to the [JUnit documentation](https://junit.org/junit5/).

## Full Usage Example
```java
import org.junit.*;

public class ExampleTestClass {

    // Variables to be used in tests
    private static int setupCount = 0;
    private int testCount = 0;

    // @BeforeClass: Executed once before any test methods. Used for setup.
    @BeforeClass
    public static void setUpClass() {
        System.out.println("Executing @BeforeClass - This runs once before any test methods.");
    }

    // @Before: Executed before each test method. Used for setup.
    @Before
    public void setUp() {
        setupCount++;
        testCount = 0;
        System.out.println("Executing @Before - This runs before each test method.");
    }

    // @Test: Denotes a test method.
    @Test
    public void testExample1() {
        testCount++;
        System.out.println("Executing @Test - Example Test 1");
        assertEquals(4, 2 + 2); // assertEquals example
        assertTrue(testCount > 0); // assertTrue example
        assertFalse(testCount > 1); // assertFalse example
        assertNotNull(this); // assertNotNull example
    }

    // @Test: Another test method
    @Test
    public void testExample2() {
        testCount++;
        System.out.println("Executing @Test - Example Test 2");
        assertNull(null); // assertNull example
        assertNotNull("not null"); // assertNotNull example
    }

    // @After: Executed after each test method. Used for cleanup.
    @After
    public void tearDown() {
        System.out.println("Executing @After - This runs after each test method.");
    }

    // @AfterClass: Executed once after all test methods. Used for cleanup.
    @AfterClass
    public static void tearDownClass() {
        System.out.println("Executing @AfterClass - This runs once after all test methods.");
    }
}
```