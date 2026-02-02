# dependency in your pubspec.yaml file
**URL:** https://flutter.dev/docs/development/packages-and-plugins/using-packages
**Page Title:** Using packages
--------------------

docs.flutter.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic.
Check out our newly published best practices for building AI-powered apps with Flutter!
Flutter supports using shared packages contributed by other developers
                  to the Flutter and Dart ecosystems. This allows quickly building
                  an app without having to develop everything from scratch.
Existing packages enable many use cases—for example,
                  making network requests ( http ),
                  navigation/route handling ( go_router ),
                  integration with device APIs
                  ( url_launcher and battery_plus ),
                  and using third-party platform SDKs like Firebase
                  ( FlutterFire ).
[LINK: FlutterFire](https://github.com/firebase/flutterfire)
To write a new package, see developing packages .
                  To add assets, images, or fonts,
                  whether stored in files or packages,
                  see Adding assets and images .

## Using packages

The following section describes how to use
                  existing published packages.

### Searching for packages

Packages are published to pub.dev .
The Flutter landing page on pub.dev displays
                  top packages that are compatible with Flutter
                  (those that declare dependencies generally compatible with Flutter),
                  and supports searching among all published packages.
The Flutter Favorites page on pub.dev lists
                  the plugins and packages that have been identified as
                  packages you should first consider using when writing
                  your app. For more information on what it means to
                  be a Flutter Favorite, see the Flutter Favorites program .
You can also browse the packages on pub.dev by filtering
                  on Android , iOS , web , Linux , Windows , macOS ,
                  or any combination thereof.

### Adding a package dependency to an app using flutter pub add

To add the package css_colors to an app:
- Use the pub add command from inside the project directory flutter pub add css_colors
Use the pub add command from inside the project directory
- flutter pub add css_colors
- Import it Add a corresponding import statement in the Dart code.
Import it
- Add a corresponding import statement in the Dart code.
- Stop and restart the app, if necessary If the package brings platform-specific code
                        (Kotlin/Java for Android, Swift/Objective-C for iOS),
                        that code must be built into your app.
                        Hot reload and hot restart only update the Dart code,
                        so a full restart of the app might be required to avoid
                        errors like MissingPluginException when using the package.
Stop and restart the app, if necessary
- If the package brings platform-specific code
                        (Kotlin/Java for Android, Swift/Objective-C for iOS),
                        that code must be built into your app.
                        Hot reload and hot restart only update the Dart code,
                        so a full restart of the app might be required to avoid
                        errors like MissingPluginException when using the package.

### Adding a package dependency to an app

To add the package css_colors to an app:
- Depend on it Open the pubspec.yaml file located inside the app folder,
                        and add css_colors: ^1.0.0 under dependencies .
Depend on it
- Open the pubspec.yaml file located inside the app folder,
                        and add css_colors: ^1.0.0 under dependencies .
- Install it From the terminal: Run flutter pub get . OR From VS Code: Click Get Packages located in right side of the action
                        ribbon at the top of pubspec.yaml indicated by the Download icon. From Android Studio/IntelliJ: Click Pub get in the action
                        ribbon at the top of pubspec.yaml .
Install it
- From the terminal: Run flutter pub get . OR
- From VS Code: Click Get Packages located in right side of the action
                        ribbon at the top of pubspec.yaml indicated by the Download icon.
- From Android Studio/IntelliJ: Click Pub get in the action
                        ribbon at the top of pubspec.yaml .
- Import it Add a corresponding import statement in the Dart code.
Import it
- Add a corresponding import statement in the Dart code.
- Stop and restart the app, if necessary If the package brings platform-specific code
                        (Kotlin/Java for Android, Swift/Objective-C for iOS),
                        that code must be built into your app.
                        Hot reload and hot restart only update the Dart code,
                        so a full restart of the app might be required to avoid
                        errors like MissingPluginException when using the package.
Stop and restart the app, if necessary
- If the package brings platform-specific code
                        (Kotlin/Java for Android, Swift/Objective-C for iOS),
                        that code must be built into your app.
                        Hot reload and hot restart only update the Dart code,
                        so a full restart of the app might be required to avoid
                        errors like MissingPluginException when using the package.

### Removing a package dependency from an app using flutter pub remove

To remove the package css_colors from an app:
- Use the pub remove command from inside the project directory flutter pub remove css_colors
- flutter pub remove css_colors
The Installing tab ,
                  available on any package page on pub.dev,
                  is a handy reference for these steps.
For a complete example,
                  see the css_colors example below.

### Conflict resolution

Suppose you want to use some_package and another_package in an app,
                  and both of these depend on url_launcher ,
                  but in different versions.
                  That causes a potential conflict.
                  The best way to avoid this is for package authors to use version ranges rather than specific versions when
                  specifying dependencies.
If some_package declares the dependencies above
                  and another_package declares a compatible url_launcher dependency like '5.4.6' or ^5.5.0 , pub resolves the issue automatically.
                  Platform-specific dependencies on Gradle modules and/or CocoaPods are solved in a similar way.
[LINK: Gradle modules](https://docs.gradle.org/current/userguide/declaring_dependencies.html)
Even if some_package and another_package declare incompatible versions for url_launcher ,
                  they might actually use url_launcher in
                  compatible ways. In this situation,
                  the conflict can be resolved by adding
                  a dependency override declaration to the app's pubspec.yaml file, forcing the use of a particular version.
For example, to force the use of url_launcher version 5.4.0 ,
                  make the following changes to the app's pubspec.yaml file:
If the conflicting dependency is not itself a package,
                  but an Android-specific library like guava ,
                  the dependency override declaration must be added to
                  Gradle build logic instead.
To force the use of guava version 28.0 , make the following
                  changes to the app's android/build.gradle file:
CocoaPods doesn't currently offer dependency
                  override functionality.

## Developing new packages

If no package exists for your specific use case,
                  you can write a custom package .

## Managing package dependencies and versions

To minimize the risk of version collisions,
                  specify a version range in the pubspec.yaml file.

### Package versions

All packages have a version number, specified in the
                  package's pubspec.yaml file. The current version of a package
                  is displayed next to its name (for example,
                  see the url_launcher package), as
                  well as a list of all prior versions
                  (see url_launcher versions ).
To ensure that the app doesn't break when you update a package,
                  specify a version range using one of the following formats.
- Ranged constraints: Specify a minimum and maximum version. yaml dependencies : url_launcher : ' >=5.4.0 <6.0.0 '
Ranged constraints: Specify a minimum and maximum version.
- Ranged constraints using the caret syntax : Specify the version that serves as the inclusive minimum version.
                      This covers all versions from that version to the next major version. yaml dependencies : collection : ' ^5.4.0 ' This syntax means the same as the one noted in the first bullet.
Ranged constraints using the caret syntax : Specify the version that serves as the inclusive minimum version.
                      This covers all versions from that version to the next major version.
This syntax means the same as the one noted in the first bullet.
To learn more, check out the package versioning guide .

### Updating package dependencies

When running flutter pub get for the first time after adding a package,
                  Flutter saves the concrete package version found in the pubspec.lock lockfile . This ensures that you get the same version again
                  if you, or another developer on your team, run flutter pub get .
To upgrade to a new version of the package,
                  for example to use new features in that package,
                  run flutter pub upgrade to retrieve the highest available version of the package
                  that is allowed by the version constraint specified in pubspec.yaml .
                  Note that this is a different command from flutter upgrade or flutter update-packages ,
                  which both update Flutter itself.

### Dependencies on unpublished packages

Packages can be used even when not published on pub.dev.
                  For private packages, or for packages not ready for publishing,
                  additional dependency options are available:
A Flutter app can depend on a package using a file system path: dependency. The path can be either relative or absolute.
                      Relative paths are evaluated relative to the directory
                      containing pubspec.yaml . For example, to depend on a
                      package, packageA, located in a directory next to the app,
                      use the following syntax:
You can also depend on a package stored in a Git repository.
                      If the package is located at the root of the repo,
                      use the following syntax:
If the repository is private and you can connect to it using SSH,
                      depend on the package by using the repo's SSH url:
Pub assumes the package is located in
                      the root of the Git repository. If that isn't
                      the case, specify the location with the path argument.
                      For example:
Finally, use the ref argument to pin the dependency to a
                      specific git commit, branch, or tag. For more details, see Package dependencies .

## Examples

The following examples walk through the necessary steps for
                  using packages.

### Example: Using the css_colors package

The css_colors package
                  defines color constants for CSS colors, so use the constants
                  wherever the Flutter framework expects the Color type.
To use this package:
- Create a new project called cssdemo .
Create a new project called cssdemo .
- Open pubspec.yaml , and add the css-colors dependency: yaml dependencies : flutter : sdk : flutter css_colors : ^1.0.0
Open pubspec.yaml , and add the css-colors dependency:
- Run flutter pub get in the terminal,
                      or click Get Packages in VS Code.
Run flutter pub get in the terminal,
                      or click Get Packages in VS Code.
- Open lib/main.dart and replace its full contents with: dart import ' package:css_colors/css_colors.dart ' ; import ' package:flutter/material.dart ' ; ​ void main ( ) { runApp ( const MyApp ( ) ) ; } ​ class MyApp extends StatelessWidget { const MyApp ( { super . key } ) ; ​ @override Widget build ( BuildContext context ) { return const MaterialApp ( home : DemoPage ( ) ) ; } } ​ class DemoPage extends StatelessWidget { const DemoPage ( { super . key } ) ; ​ @override Widget build ( BuildContext context ) { return Scaffold ( body : Container ( color : CSSColors . orange ) ) ; } }
Open lib/main.dart and replace its full contents with:
- Run the app. The app's background should now be orange.
Run the app. The app's background should now be orange.

### Example: Using the url_launcher package to launch the browser

The url_launcher plugin package enables opening
                  the default browser on the mobile platform to display
                  a given URL, and is supported on Android, iOS, web,
                  Windows, Linux, and macOS.
                  This package is a special Dart package called a plugin package (or plugin ),
                  which includes platform-specific code.
To use this plugin:
- Create a new project called launchdemo .
Create a new project called launchdemo .
- Open pubspec.yaml , and add the url_launcher dependency: yaml dependencies : flutter : sdk : flutter url_launcher : ^5.4.0
Open pubspec.yaml , and add the url_launcher dependency:
- Run flutter pub get in the terminal,
                      or click Get Packages get in VS Code.
Run flutter pub get in the terminal,
                      or click Get Packages get in VS Code.
- Open lib/main.dart and replace its full contents with the
                      following: dart import ' package:flutter/material.dart ' ; import ' package:url_launcher/url_launcher.dart ' ; ​ void main ( ) { runApp ( const MyApp ( ) ) ; } ​ class MyApp extends StatelessWidget { const MyApp ( { super . key } ) ; ​ @override Widget build ( BuildContext context ) { return const MaterialApp ( home : DemoPage ( ) ) ; } } ​ class DemoPage extends StatelessWidget { const DemoPage ( { super . key } ) ; ​ void launchURL ( ) { launchUrl ( Uri . parse ( ' https://flutter.dev ' ) ) ; } ​ @override Widget build ( BuildContext context ) { return Scaffold ( body : Center ( child : ElevatedButton ( onPressed : launchURL , child : const Text ( ' Show Flutter homepage ' ) , ) , ) , ) ; } }
Open lib/main.dart and replace its full contents with the
                      following:
- Run the app (or stop and restart it, if it was already running
                      before adding the plugin). Click Show Flutter homepage .
                      You should see the default browser open on the device,
                      displaying the homepage for flutter.dev.
Run the app (or stop and restart it, if it was already running
                      before adding the plugin). Click Show Flutter homepage .
                      You should see the default browser open on the device,
                      displaying the homepage for flutter.dev.
Unless stated otherwise, the documentation on this site reflects Flutter 3.38.6. Page last updated on 2025-12-18. View source or report an issue .
[LINK: View source](https://github.com/flutter/website/blob/main/src/content/packages-and-plugins/using-packages.md)
[LINK: report an issue](https://github.com/flutter/website/issues/new?template=1_page_issue.yml&page-url=https://docs.flutter.dev/packages-and-plugins/using-packages&page-source=https://github.com/flutter/website/blob/main/src/content/packages-and-plugins/using-packages.md)

--------------------