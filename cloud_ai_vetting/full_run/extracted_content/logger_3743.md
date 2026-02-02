# Logger
**URL:** https://ruby-doc.org/3.2.2/stdlibs/logger/Logger.html
**Page Title:** class Logger - logger: Ruby Standard Library Documentation
--------------------

- Home
- 3.2.2
- Downloads
- Dark mode

## class Logger

Class Logger provides a simple but sophisticated logging utility that you can use to create one or more event logs for your program. Each such log contains a chronological sequence of entries that provides a record of the program’s activities.

## About the Examples ¶ ↑

All examples on this page assume that Logger has been required:

## Synopsis ¶ ↑

Create a log with Logger.new :
Add entries (level, message) with Logger#add :
Close the log with Logger#close :

## Entries ¶ ↑

You can add entries with method Logger#add :
These shorthand methods also add entries:
When you call any of these methods, the entry may or may not be written to the log, depending on the entry’s severity and on the log level; see Log Level
An entry always has:
- A severity (the required argument to add ).
A severity (the required argument to add ).
- An automatically created timestamp.
An automatically created timestamp.
And may also have:
- A message.
A message.
- A program name.
A program name.
Example:
The default format for an entry is:
where the values to be formatted are:
- Severity (one letter).
Severity (one letter).
- Timestamp.
Timestamp.
- Process id.
Process id.
- Severity (word).
Severity (word).
- Program name.
Program name.
- Message.
Message.
You can use a different entry format by:
- Setting a custom format proc (affects following entries); see formatter= .
Setting a custom format proc (affects following entries); see formatter= .
- Calling any of the methods above with a block (affects only the one entry). Doing so can have two benefits: Context: the block can evaluate the entire program context and create a context-dependent message. Performance: the block is not evaluated unless the log level permits the entry actually to be written: logger . error { my_slow_message_generator } Contrast this with the string form, where the string is always evaluated, regardless of the log level: logger . error ( "#{my_slow_message_generator}" )
Calling any of the methods above with a block (affects only the one entry). Doing so can have two benefits:
- Context: the block can evaluate the entire program context and create a context-dependent message.
Context: the block can evaluate the entire program context and create a context-dependent message.
- Performance: the block is not evaluated unless the log level permits the entry actually to be written: logger . error { my_slow_message_generator } Contrast this with the string form, where the string is always evaluated, regardless of the log level: logger . error ( "#{my_slow_message_generator}" )
Performance: the block is not evaluated unless the log level permits the entry actually to be written:
Contrast this with the string form, where the string is always evaluated, regardless of the log level:

### Severity ¶ ↑

The severity of a log entry has two effects:
- Determines whether the entry is selected for inclusion in the log; see Log Level .
Determines whether the entry is selected for inclusion in the log; see Log Level .
- Indicates to any log reader (whether a person or a program) the relative importance of the entry.
Indicates to any log reader (whether a person or a program) the relative importance of the entry.

### Timestamp ¶ ↑

The timestamp for a log entry is generated automatically when the entry is created.
The logged timestamp is formatted by method Time#strftime using this format string:
Example:
You can set a different format using method datetime_format= .

### Message ¶ ↑

The message is an optional argument to an entry method:
For the default entry formatter, Logger::Formatter , the message object may be:
- A string: used as-is.
A string: used as-is.
- An Exception: message.message is used.
An Exception: message.message is used.
- Anything else: message.inspect is used.
Anything else: message.inspect is used.
Note : Logger::Formatter does not escape or sanitize the message passed to it. Developers should be aware that malicious data (user input) may be in the message, and should explicitly escape untrusted data.
You can use a custom formatter to escape message data; see the example at formatter= .

### Program Name ¶ ↑

The program name is an optional argument to an entry method:
The default program name for a new logger may be set in the call to Logger.new via optional keyword argument progname :
The default program name for an existing logger may be set by a call to method progname= :
The current program name may be retrieved with method progname :

## Log Level ¶ ↑

The log level setting determines whether an entry is actually written to the log, based on the entry’s severity.
These are the defined severities (least severe to most severe):
The default initial level setting is Logger::DEBUG, the lowest level, which means that all entries are to be written, regardless of severity:
You can specify a different setting in a new logger using keyword argument level with an appropriate value:
With this level, entries with severity Logger::ERROR and higher are written, while those with lower severities are not written:
You can set the log level for an existing logger with method level= :
These shorthand methods also set the level:
You can retrieve the log level with method level :
These methods return whether a given level is to be written:

## Log File Rotation ¶ ↑

By default, a log file is a single file that grows indefinitely (until explicitly closed); there is no file rotation.
To keep log files to a manageable size, you can use log file rotation , which uses multiple log files:
- Each log file has entries for a non-overlapping time interval.
Each log file has entries for a non-overlapping time interval.
- Only the most recent log file is open and active; the others are closed and inactive.
Only the most recent log file is open and active; the others are closed and inactive.

### Size-Based Rotation ¶ ↑

For size-based log file rotation, call Logger.new with:
- Argument logdev as a file path.
Argument logdev as a file path.
- Argument shift_age with a positive integer: the number of log files to be in the rotation.
Argument shift_age with a positive integer: the number of log files to be in the rotation.
- Argument shift_size as a positive integer: the maximum size (in bytes) of each log file; defaults to 1048576 (1 megabyte).
Argument shift_size as a positive integer: the maximum size (in bytes) of each log file; defaults to 1048576 (1 megabyte).
Examples:
For these examples, suppose:
Logging begins in the new log file, t.log ; the log file is “full” and ready for rotation when a new entry would cause its size to exceed shift_size .
The first time t.log is full:
- t.log is closed and renamed to t.log.0 .
t.log is closed and renamed to t.log.0 .
- A new file t.log is opened.
A new file t.log is opened.
The second time t.log is full:
- +t.log.0 is renamed as t.log.1 .
+t.log.0 is renamed as t.log.1 .
- t.log is closed and renamed to t.log.0 .
t.log is closed and renamed to t.log.0 .
- A new file t.log is opened.
A new file t.log is opened.
Each subsequent time that t.log is full, the log files are rotated:
- t.log.1 is removed.
t.log.1 is removed.
- +t.log.0 is renamed as t.log.1 .
+t.log.0 is renamed as t.log.1 .
- t.log is closed and renamed to t.log.0 .
t.log is closed and renamed to t.log.0 .
- A new file t.log is opened.
A new file t.log is opened.

### Periodic Rotation ¶ ↑

For periodic rotation, call Logger.new with:
- Argument logdev as a file path.
Argument logdev as a file path.
- Argument shift_age as a string period indicator.
Argument shift_age as a string period indicator.
Examples:
Example:
When the given period expires:
- The base log file, t.log is closed and renamed with a date-based suffix such as t.log.20220509 .
The base log file, t.log is closed and renamed with a date-based suffix such as t.log.20220509 .
- A new log file t.log is opened.
A new log file t.log is opened.
- Nothing is removed.
Nothing is removed.
The default format for the suffix is '%Y%m%d' , which produces a suffix similar to the one above. You can set a different format using create-time option shift_period_suffix ; see details and suggestions at Time#strftime.
Severity label for logging (max 5 chars).
Sets or retrieves the logger entry formatter proc.
When formatter is nil , the logger uses Logger::Formatter .
When formatter is a proc, a new entry is formatted by the proc, which is called with four arguments:
- severity : The severity of the entry.
severity : The severity of the entry.
- time : A Time object representing the entry’s timestamp.
time : A Time object representing the entry’s timestamp.
- progname : The program name for the entry.
progname : The program name for the entry.
- msg : The message for the entry (string or string-convertible object).
msg : The message for the entry (string or string-convertible object).
The proc should return a string containing the formatted entry.
This custom formatter uses String#dump to escape the message string:
Output:
Logging severity threshold (e.g. Logger::INFO ).
Program name to include in log messages.
Logging severity threshold (e.g. Logger::INFO ).
With the single argument logdev , returns a new logger with all default options:
Argument logdev must be one of:
- A string filepath: entries are to be written to the file at that path; if the file at that path exists, new entries are appended.
A string filepath: entries are to be written to the file at that path; if the file at that path exists, new entries are appended.
- An IO stream (typically +$stdout+, +$stderr+. or an open file): entries are to be written to the given stream.
An IO stream (typically +$stdout+, +$stderr+. or an open file): entries are to be written to the given stream.
- nil or File::NULL : no entries are to be written.
nil or File::NULL : no entries are to be written.
Examples:
The keyword options are:
- level : sets the log level; default value is Logger::DEBUG. See Log Level : Logger . new ( 't.log' , level: Logger :: ERROR )
level : sets the log level; default value is Logger::DEBUG. See Log Level :
- progname : sets the default program name; default is nil . See Program Name : Logger . new ( 't.log' , progname: 'mung' )
progname : sets the default program name; default is nil . See Program Name :
- formatter : sets the entry formatter; default is nil . See formatter= .
formatter : sets the entry formatter; default is nil . See formatter= .
- datetime_format : sets the format for entry timestamp; default is nil . See datetime_format= .
datetime_format : sets the format for entry timestamp; default is nil . See datetime_format= .
- binmode : sets whether the logger writes in binary mode; default is false .
binmode : sets whether the logger writes in binary mode; default is false .
- shift_period_suffix : sets the format for the filename suffix for periodic log file rotation; default is '%Y%m%d' . See Periodic Rotation .
shift_period_suffix : sets the format for the filename suffix for periodic log file rotation; default is '%Y%m%d' . See Periodic Rotation .
Writes the given msg to the log with no formatting; returns the number of characters written, or nil if no log device exists:
Output:
Creates a log entry, which may or may not be written to the log, depending on the entry’s severity and on the log level. See Log Level and Entries for details.
Examples:
Output:
These convenience methods have implicit severity:
- debug .
debug .
- info .
info .
- warn .
warn .
- error .
error .
- fatal .
fatal .
- unknown .
unknown .
Closes the logger; returns nil :
Related: Logger#reopen .
Returns the date-time format; see datetime_format= .
Sets the date-time format.
Argument datetime_format should be either of these:
- A string suitable for use as a format for method Time#strftime.
A string suitable for use as a format for method Time#strftime.
- nil : the logger uses '%Y-%m-%dT%H:%M:%S.%6N' .
nil : the logger uses '%Y-%m-%dT%H:%M:%S.%6N' .
Equivalent to calling add with severity Logger::DEBUG .
Sets the log level to Logger::DEBUG. See Log Level .
Returns true if the log level allows entries with severity Logger::DEBUG to be written, false otherwise. See Log Level .
Equivalent to calling add with severity Logger::ERROR .
Sets the log level to Logger::ERROR. See Log Level .
Returns true if the log level allows entries with severity Logger::ERROR to be written, false otherwise. See Log Level .
Equivalent to calling add with severity Logger::FATAL .
Sets the log level to Logger::FATAL. See Log Level .
Returns true if the log level allows entries with severity Logger::FATAL to be written, false otherwise. See Log Level .
Equivalent to calling add with severity Logger::INFO .
Sets the log level to Logger::INFO. See Log Level .
Returns true if the log level allows entries with severity Logger::INFO to be written, false otherwise. See Log Level .
Sets the log level; returns severity . See Log Level .
Argument severity may be an integer, a string, or a symbol:
Logger#sev_threshold= is an alias for Logger#level= .
Sets the logger’s output stream:
- If logdev is nil , reopens the current output stream.
If logdev is nil , reopens the current output stream.
- If logdev is a filepath, opens the indicated file for append.
If logdev is a filepath, opens the indicated file for append.
- If logdev is an IO stream (usually $stdout , $stderr , or an open File object), opens the stream for append.
If logdev is an IO stream (usually $stdout , $stderr , or an open File object), opens the stream for append.
Example:
Equivalent to calling add with severity Logger::UNKNOWN .
Equivalent to calling add with severity Logger::WARN .
Sets the log level to Logger::WARN. See Log Level .
Returns true if the log level allows entries with severity Logger::WARN to be written, false otherwise. See Log Level .

--------------------