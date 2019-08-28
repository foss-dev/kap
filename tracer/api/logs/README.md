# Logs Layer

In this layer, we'll do operations in the [features](#features) section.

## Features

- Application Logs
- Application Log Details (If possible elaborate explanation or StackOverflow URL etc.)
- Application Log Filtering

## Info

All data operations work in controllers.py file. User requests are also coming here. 

### Exception Data

Programming languages have different exception objects. We must have some required data these are should be like this

#### PHP

- Exception Message
- Exception File
- Exception Code
- Exception Line
- Exception Type

**Exception object for PHP**

[http://php.net/manual/tr/class.exception.php](http://php.net/manual/tr/class.exception.php)

```php
 Exception implements Throwable {
    
    protected string $message ;
    protected int $code ;
    protected string $file ;
    protected int $line ;
    
    //...
    final public getMessage ( void ) : string
    final public getPrevious ( void ) : Throwable
    final public getCode ( void ) : mixed
    final public getFile ( void ) : string
    final public getLine ( void ) : int
    final public getTrace ( void ) : array
    final public getTraceAsString ( void ) : string
    public __toString ( void ) : string
    final private __clone ( void ) : void
}
```

#### C#

- Data 	
- HelpLink 	
- HResult 	
- InnerException 	
- Message 	
- Source 	
- StackTrace 	
- TargetSite
- Exception Type

In **C#** you can get error like like this

[https://stackoverflow.com/a/3329072/3821823](https://stackoverflow.com/a/3329072/3821823)

```cs
try
{
    throw new Exception();
}
catch (Exception ex)
{
    // Get stack trace for the exception with source file information
    var st = new StackTrace(ex, true);
    // Get the top stack frame
    var frame = st.GetFrame(0);
    // Get the line number from the stack frame
    var line = frame.GetFileLineNumber();
}
```

#### JavaScript

JavaScript have different error properties but they the same as other languages'. Errors are thrown by `Error` object.

[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/prototype](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/prototype)

- File Name
- Line Number
- Column Number
- Stack
- Error Type

An example for JavaScript

```js
try {
  foo.bar();
} catch (e) {
  if (e instanceof EvalError) {
    console.log(e.name + ': ' + e.message);
  } else if (e instanceof RangeError) {
    console.log(e.name + ': ' + e.message);
  }
  // ... etc
}
```