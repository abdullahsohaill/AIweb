# Tenacity
**URL:** https://tenacity.readthedocs.io/en/latest
**Page Title:** Tenacity — Tenacity documentation
--------------------

- Docs »
- Tenacity
- Edit on GitHub
[LINK: Edit on GitHub](https://github.com/jd/tenacity/blob/master/doc/source/index.rst)

## Tenacity ¶

Please refer to the tenacity documentation for a better experience.
[LINK: tenacity documentation](https://tenacity.readthedocs.io/en/latest/)
Tenacity is an Apache 2.0 licensed general-purpose retrying library, written in
Python, to simplify the task of adding retry behavior to just about anything.
It originates from a fork of retrying which is sadly no longer maintained . Tenacity isn’t
api compatible with retrying but adds significant new functionality and
fixes a number of longstanding bugs.
[LINK: a fork of retrying](https://github.com/rholder/retrying/issues/65)
The simplest use case is retrying a flaky function whenever an Exception occurs until a value is returned.

## Features ¶

- Generic Decorator API
- Specify stop condition (i.e. limit by number of attempts)
- Specify wait condition (i.e. exponential backoff sleeping between attempts)
- Customize retrying on Exceptions
- Customize retrying on expected returned result
- Retry on coroutines
- Retry code block with context manager

## Installation ¶

To install tenacity , simply:

## Examples ¶

### Basic Retry ¶

As you saw above, the default behavior is to retry forever without waiting when
an exception is raised.

### Stopping ¶

Let’s be a little less persistent and set some boundaries, such as the number
of attempts before giving up.
We don’t have all day, so let’s set a boundary for how long we should be
retrying stuff.
You can combine several stop conditions by using the | operator:

### Waiting before retrying ¶

Most things don’t like to be polled as fast as possible, so let’s just wait 2
seconds between retries.
Some things perform best with a bit of randomness injected.
Then again, it’s hard to beat exponential backoff when retrying distributed
services and other remote endpoints.
Then again, it’s also hard to beat combining fixed waits and jitter (to
help avoid thundering herds) when retrying distributed services and other
remote endpoints.
When multiple processes are in contention for a shared resource, exponentially
increasing jitter helps minimise collisions.
Sometimes it’s necessary to build a chain of backoffs.

### Whether to retry ¶

We have a few options for dealing with retries that raise specific or general
exceptions, as in the cases here.
We can also use the result of the function to alter the behavior of retrying.
See also these methods:
We can also combine several conditions:
Any combination of stop, wait, etc. is also supported to give you the freedom
to mix and match.
It’s also possible to retry explicitly at any time by raising the TryAgain exception:

### Error Handling ¶

Normally when your function fails its final time (and will not be retried again based on your settings),
a RetryError is raised. The exception your code encountered will be shown somewhere in the middle of the stack trace.
If you would rather see the exception your code encountered at the end of the stack trace (where it
is most visible), you can set reraise=True .

### Before and After Retry, and Logging ¶

It’s possible to execute an action before any attempt of calling the function
by using the before callback function:
In the same spirit, It’s possible to execute after a call that failed:
It’s also possible to only log failures that are going to be retried. Normally
retries happen after a wait interval, so the keyword argument is called before_sleep :

### Statistics ¶

You can access the statistics about the retry made over a function by using the retry attribute attached to the function and its statistics attribute:

### Custom Callbacks ¶

You can also define your own callbacks. The callback should accept one
parameter called retry_state that contains all information about current
retry invocation.
For example, you can call a custom callback function after all retries failed,
without raising an exception (or you can re-raise or do anything really)

### RetryCallState ¶

retry_state argument is an object of RetryCallState class:
State related to a single call wrapped with Retrying.
Constant attributes:
Variable attributes:

### Other Custom Callbacks ¶

It’s also possible to define custom callbacks for other keyword arguments.
Here’s an example with a custom before_sleep function:

### Changing Arguments at Run Time ¶

You can change the arguments of a retry decorator as needed when calling it by
using the retry_with function attached to the wrapped function:
If you want to use variables to set up the retry parameters, you don’t have
to use the retry decorator - you can instead use Retrying directly:

### Retrying code block ¶

Tenacity allows you to retry a code block without the need to wraps it in an
isolated function. This makes it easy to isolate failing block while sharing
context. The trick is to combine a for loop and a context manager.
You can configure every details of retry policy by configuring the Retrying
object.
With async code you can use AsyncRetrying.
In both cases, you may want to set the result to the attempt so it’s available
in retry strategies like retry_if_result . This can be done accessing the retry_state property:

### Async and retry ¶

Finally, retry works also on asyncio and Tornado (>= 4.5) coroutines.
Sleeps are done asynchronously too.
You can even use alternative event loops such as curio or Trio by passing the correct sleep function:

## Contribute ¶

- Check for open issues or open a fresh issue to start a discussion around a
feature idea or a bug.
- Fork the repository on GitHub to start making your changes to the main branch (or branch off of it).
[LINK: the repository](https://github.com/jd/tenacity)
- Write a test which shows that the bug was fixed or that the feature works as
expected.
- Add a changelog
- Make the docs better (or more detailed, or more easier to read, or …)

### Changelogs ¶

reno is used for managing changelogs. Take a look at their usage docs.
[LINK: reno](https://docs.openstack.org/reno/latest/user/usage.html)
The doc generation will automatically compile the changelogs. You just need to add them.

--------------------