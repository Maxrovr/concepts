# SOLID Principles

There are five SOLID principles:

1. Single Responsibility Principle (SRP)    
2. Open Closed Principle (OCP)
3. Liskov Substitution Principle (LSP)
4. Interface Segregation Principle (ISP)
5. Dependency Inversion Principle (DIP)

---

## Single Responsibility Principle (SRP)

**A class should have only one reason to change.** 

A class should not be loaded with multiple responsibilities and a single responsibility should not be spread across multiple classes or mixed with other responsibilities. The reason is that more changes requested in the future, the more changes the class need to apply.

### Bad Way

This Add method does too much, it shouldn’t know how to write to the log and how to add a customer.

```
class Customer
{
    void Add(Database db)
    {
        try
        {
            db.Add();
        }
        catch (Exception ex)
        {
            File.WriteAllText(@"C:\Error.txt", ex.ToString());
        }
    }
}
```
### Good Way

This doesn’t violate the single responsibility principle by abstracting the logger for the actual writing.

```
class Customer
{
    private FileLogger logger = new FileLogger();
    void Add(Database db)
    {
        try {
            db.Add();
        }
        catch (Exception ex)
        {
            logger.Handle(ex.ToString());
        }
    }
}
class FileLogger
{
    void Handle(string error)
    {
        File.WriteAllText(@"C:\Error.txt", error);
    }
}

```
---

## Open Closed Principle
 
**Open for Extension Closed for Modification. Prefer extension over modification.**

### Bad Way

This example violates the Open Closed Principle, because at the moment there are 2 types of customer, if we want to add another customer type we have to add an if else statement below and will modify the existing code.

```
class Customer
{
    int Type;

    void Add(Database db)
    {
        if (Type == 0)
        {
            db.Add();
        }
        else
        {
            db.AddExistingCustomer();
        }
    }
}
```

### Good Way

This is better, because we structure the code so it’s easier to extend and harder to modify.

```
class CustomerBetter
{
    void Add(Database db)
    {
        db.Add();
    }
}

class ExistingCustomer : CustomerBetter
{
    override void Add(Database db)
    {
        db.AddExistingCustomer();
    }
}

class AnotherCustomer : CustomerBetter
{
    override void Add(Database db)
    {
        db.AnotherExtension();
    }
}
```

---


## Liskov Substitution Principle (LSP)

**The parent class should be able to refer child objects seamlessly during runtime polymorphism.** 

### Bad Way

This violates Liskov substitution principle. The parent should easily replace the child object and not break any functionality, only lose some, e.g. for this example below, we don’t want this to add an enquiry so we have to throw a new exception, that violates the principle.

```
class Enquiry : Customer
{
    override int Discount(int sales)
    {
        return sales * 5;
    }

    override void Add(Database db)
    {
        throw new Exception("Not allowed");
    }
}

class BetterGoldCustomer : Customer
{
    override int Discount(int sales)
    {
        return sales - 100;
    }
}

class BetterSilverCustomer : Customer
{
    override int Discount(int sales)
    {
        return sales - 50;
    }
}

// e.g. to show how this is bad:
class ViolatingLiskovs
{
    void ParseCustomers()
    {
        var database = new Database();
        var customers = new List<Customer>
        {
            new GoldCustomer(),
            new SilverCustomer(),
            new Enquiry() // This is valid, but...
        };

        foreach (Customer c in customers)
        {
            // Enquiry.Add() will throw an exception here!
            c.Add(database);
        }
    }
}

```

### Good Way
```
interface IDiscount {
    int Discount(int sales);
}

interface IDatabase {
    void Add(Database db);
}

internal class Customer : IDiscount, IDatabase
{
    int Discount(int sales) { return sales; }
    void Add(Database db) { db.Add(); }
}

// GOOD: Now, we don't violate Liskov Substitution principle
class AdheringToLiskovs
{
    public void ParseCustomers()
    {
        var database = new Database();
        var customers = new List<Customer>
        {
            new GoldCustomer(),
            new SilverCustomer(),
            new Enquiry() // This will give a compiler error, rather than runtime error
        };

        foreach (Customer c in customers)
        {
            // Enquiry.Add() will throw an exception here!
            // But, we won't get to here as compiler will complain
            c.Add(database);
        }
    }
}

```

---


## Interface Segregation Principle

**A client should not be forced to use an interface, if it doesn’t need it.**

### Bad Way

If we want to add more functionality, don’t add to existing interfaces, segregate them out.
```
interface ICustomer // existing
{
    void Add();
}

interface ICustomerImproved
{
    void Add(); // Existing Functionality, BAD
    void Read(); 
}
```

### Good Way

Just create another interface, that a class can also extend from.

```
interface ICustomerV1 : ICustomer
{
    void Read();
}

class CustomerWithRead : ICustomer, ICustomerV1
{
    void Add()
    {
        var customer = new Customer();
        customer.Add(new Database());
    }

    void Read()
    {
        // GOOD: New functionality here!
    }
}

// e.g.
void ManipulateCustomers()
{
    var database = new Database();
    var customer = new Customer();
    customer.Add(database); // Old functionality, works fine
    var readCustomer = new CustomerWithRead();
    readCustomer.Read(); // Good! New functionalty is separate from existing customers
}
```

---


## Dependency Inversion

**High level modules should not depend on low-level modules, but should depend on abstraction.**

### Bad Way

We are relying on the customer to say that we are using a File Logger, rather than another type of logger, e.g. EmailLogger.

```
class FileLogger
{
    void Handle(string error)
    {
        File.WriteAllText(@"C:\Error.txt", error);
    }
}

internal class Customer
{
    FileLogger logger = new FileLogger(); // Bad

    public void Add(Database db)
    {
        try
        {
            db.Add();
        }
        catch (Exception error)
        {
            logger.Handle(error.ToString());
        }
    }
}
```
### Good Way

We pass in a Logger interface to the customer so it doesn’t know what type of logger it is.

```
class BetterCustomer
{
    ILogger logger;
    BetterCustomer(ILogger logger)
    {
        this.logger = logger;
    }

    void Add(Database db)
    {
        try
        {
            db.Add();
        }
        catch (Exception error)
        {
            logger.Handle(error.ToString());
        }
    }
}
class EmailLogger : ILogger
{
    void Handle(string error)
    {
        File.WriteAllText(@"C:\Error.txt", error);
    }
}

interface ILogger
{
    void Handle(string error);
}

// e.g. when it is used:
void UseDependencyInjectionForLogger()
{
    var customer = new BetterCustomer(new EmailLogger());
    customer.Add(new Database());
}
```
---