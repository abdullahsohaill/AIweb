# Pusher
**URL:** https://pusher.com
**Page Title:** Pusher | Leader In Realtime Technologies
--------------------

- Products Build scalable realtime features Programmatic push notifications
- Build scalable realtime features
Build scalable realtime features
- Programmatic push notifications
Programmatic push notifications
- Developers Docs Read the docs to learn how to use our products Tutorials Explore our tutorials to build apps with Pusher products Support Reach out to our support team for help and advice Glossary Get familiar with Pusher-specific terminology
[LINK: Docs Read the docs to learn how to use our products](https://pusher.com/docs)
- Docs Read the docs to learn how to use our products
Read the docs to learn how to use our products
- Tutorials Explore our tutorials to build apps with Pusher products
Explore our tutorials to build apps with Pusher products
[LINK: Support Reach out to our support team for help and advice](https://docs.bird.com/pusher)
- Support Reach out to our support team for help and advice
Reach out to our support team for help and advice
- Glossary Get familiar with Pusher-specific terminology
Get familiar with Pusher-specific terminology
- User stories
- Blog
- Pricing Build scalable realtime features Programmatic push notifications
- Build scalable realtime features
Build scalable realtime features
- Programmatic push notifications
Programmatic push notifications
- Sign in

## Powering realtime experiences for mobile and web

Bi-directional hosted APIs that are flexible, scalable and easy to use. We create and maintain complex messaging infrastructure so you can build the realtime features your users need, fast.
Bi-directional hosted APIs that are flexible, scalable and easy to use.
Get started today and find out what you can build with Pusher

## Publish

$pusher -> trigger ( 'my-channel' , 'my-event' , [
'message' => 'hello world'
]);
$pusher -> trigger ( 'my-channel' , 'my-event' , [
'message' => 'hello world'
]);
pusher. trigger ( 'my-channel' , 'my-event' , {
"message" : "hello world"
});
pusher. trigger ( 'my-channel' , 'my-event' , {
message : 'hello world'
pusher. Trigger ( 'my-channel' , 'my-event' , new {
message = "hello world"
});
pusher. trigger ( "my-channel" , "my-event" , Collections . singletonMap ( "message" , "hello world" ));
pusher. trigger ( 'my-channel' , 'my-event' , {
'message' : 'hello world'
pusher.Trigger( "my-channel" , "my-event" , map[ string ] string {
"message" : "hello world" ,

## Subscribe

var channel = pusher. subscribe ( 'my-channel' );
channel. bind ( 'my-event' , function ( data ) {
alert( 'Received my-event with message: ' + data .message);
});
var channel = pusher. subscribe ( 'my-channel' );
channel. bind ( 'my-event' , function ( data ) {
alert( 'Received my-event with message: ' + data .message);
});
Channel channel = pusher. subscribe ( "my-channel" );
channel. bind ( "my-event" , new SubscriptionEventListener () {
@Override
public void onEvent ( String channel, String event, String data ) {
System.put.println( "Received event with data: " + data );
});
let channel = pusher. subscribe ( "my-channel" )
channel. bind ( eventName : "my-event" , callback : { ( optionalData : Any?) -> Void in
if let data = optionalData {
print ( "Received event with data: \(data) " )
PusherChannel *channel = [pusher subscribeWithChannelName :@ "my-channel" ];
[channel bindWithEventName: @"my-event" callback:^ void ( NSDictionary *data) {
NSString *message = data [@ "message" ];
NSLog (@ "message received: %@" , message);
}];

## Publish API

const beamsClient = new PushNotifications ({
instanceId : 'YOUR_INSTANCE_ID_HERE' ,
secretKey : 'YOUR_SECRET_KEY_HERE'
});
beamsClient. publishToInterests ([ 'hello' ], {
apns: {
aps: {
alert : 'Hello!'
fcm: {
notification: {
title : 'Hello' ,
body : 'Hello, world!'
}). then ( ( publishResponse ) => {
console . log ( 'Just published:' , publishResponse. publishId );
}). catch ( ( error ) => {
console . error ( 'Error:' , error);
});
const beamsClient = new PushNotifications ({
instanceId : 'YOUR_INSTANCE_ID_HERE' ,
secretKey : 'YOUR_SECRET_KEY_HERE'
});
beamsClient. publishToInterests ([ 'hello' ], {
apns: {
aps: {
alert : 'Hello!'
fcm: {
notification: {
title : 'Hello' ,
body : 'Hello, world!'
}). then ( ( publishResponse ) => {
console . log ( 'Just published:' , publishResponse. publishId );
}). catch ( ( error ) => {
console . error ( 'Error:' , error);
});
const (
instanceId = "YOUR_INSTANCE_ID_HERE"
secretKey  = "YOUR_SECRET_KEY_HERE"
beamsClient := pushnotifications.New(instanceId, secretKey)
publishRequest := map[ string ] interface {}{
"apns" : map[ string ] interface {}{
"aps" : map[ string ] interface {}{
"alert" : map[ string ] interface {}{
"title" : "Hello" ,
"body" : "Hello, world" ,
"fcm" : map[ string ] interface {}{
"notification" : map[ string ] interface {}{
"title" : "Hello" ,
"body" : "Hello, world" ,
pubId, err := beamsClient.PublishToInterests([] string { "hello" }, publishRequest)
if err != nil {
fmt.Println(err)
} else {
fmt. Println ( "Publish Id:" , pubId)
beams_client = PushNotifications(
instance_id= 'YOUR_INSTANCE_ID_HERE' ,
secret_key= 'YOUR_SECRET_KEY_HERE' ,
response = beams_client.publish_to_interests(
interests=[ 'hello' ],
publish_body={
'apns' : {
'aps' : {
'alert' : 'Hello!' ,
'fcm' : {
'notification' : {
'title' : 'Hello' ,
'body' : 'Hello, world!' ,
print (response[ 'publishId' ])
String instanceId = "YOUR_INSTANCE_ID_HERE" ;
String secretKey = "YOUR_SECRET_KEY_HERE" ;
PushNotifications beamsClient = new PushNotifications (instanceId, secretKey);
List < String > interests = Arrays . asList ( "donuts" , "pizza" );
Map < String , Map > publishRequest = new HashMap ();
Map < String , String > alert = new HashMap ();
alert. put ( "alert" , "hi" );
Map < String , Map > aps = new HashMap ();
aps. put ( "aps" , alert);
publishRequest. put ( "apns" , aps);
Map < String , String > fcmNotification = new HashMap ();
fcmNotification. put ( "title" , "hello" );
fcmNotification. put ( "body" , "Hello world" );
Map < String , Map > fcm = new HashMap ();
fcm. put ( "notification" , fcmNotification);
publishRequest. put ( "fcm" , fcm);
beamsClient.publishToInterests(interests, publishRequest);
val instanceId = "YOUR_INSTANCE_ID_HERE"
val secretKey = "YOUR_SECRET_KEY_HERE"
val beamsClient = PushNotifications(instanceId, secretKey)
val interests = listOf( "donuts" , "pizza" )
val publishRequest = hashMapOf(
"apns" to hashMapOf ( "aps" to hashMapOf ( "alert" to "hi" )),
"fcm" to hashMapOf ( "notification" to hashMapOf ( "title" to "hello" , "body" to "Hello world" ))
beamsClient.publishToInterests(interests, publishRequest)
Pusher :: PushNotifications .configure do |config|
config. instance_id = 'YOUR_INSTANCE_ID_HERE'
config. secret_key = 'YOUR_SECRET_KEY_HERE'
end
data = {
apns: {
aps: {
alert: {
title : 'Hello' ,
body : 'Hello, world!'
fcm: {
notification: {
title : 'Hello' ,
body : 'Hello, world!'
Pusher :: PushNotifications . publishToInterests ( interests : [ 'hello' ], payload : data)

### Trusted by Giants. Loved by developers.

### What can you build with Pusher?

From dashboards to stock charts, update data instantly
Critical transactional information, delivered every time
From food delivery to order status, realtime updates at scale
Bring delightful conversational experiences to all your users
Nick Tyler
Director of Engineering, GoGuardian
Connor Thielmann
VP of Business Operations, ServiceTitan
Jeremy Bowers
Director of Engineering, The Washington Post
Peter Hamilton
Head of Technology, Remind

### We have everything you need to get you set up

### Docs

Full reference of our APIs

### Tutorials

Tutorials to help you get started

### 40+ SDKs

Bring our APIs to any tech stack

## Start building with Pusher

## Pusher is a member of the MessageBird team

As of November 2020, we have become part of MessageBird. With the weight of the world's largest omnichannel communications platform behind us, the Pusher team remains focused on building developer-led features at scale.

## Products

- Channels
- Beams

## Developers

- Docs
[LINK: Docs](https://pusher.com/docs)
- Tutorials
- Status
- Support
[LINK: Support](https://docs.bird.com/pusher)
- Sessions
- Glossary

## Company

- Contact Sales
- User stories
- Support
- Blog
- Careers Hiring

## Legal

- Terms & Conditions
- Cookie Policy
- Privacy Policy
- Contests
- Quotas
- Security
- Code of Conduct
© 2025 Pusher Ltd. All rights reserved. Pusher Limited is a company registered in England and Wales (No. 07489873) whose registered office is at MessageBird UK Limited, 3 More London Riverside, 4th Floor, London, United Kingdom, SE1 2AQ.

--------------------