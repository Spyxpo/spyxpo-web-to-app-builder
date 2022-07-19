// don't change the source code, this is a very important file

import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_webview_pro/webview_flutter.dart';
import 'package:url_launcher/url_launcher.dart';
import 'screens/screens.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Example',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      debugShowCheckedModeBanner: false,
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  void initState() {
    super.initState();
    if (Platform.isAndroid) WebView.platform = AndroidWebView();
  }

  @override
  Widget build(BuildContext context) {
    String url = 'https://www.spyxpo.com';
    return SafeArea(
      child: Scaffold(
        body: Builder(builder: (BuildContext context) {
          return WebView(
            initialUrl: url,
            javascriptMode: JavascriptMode.unrestricted,
            onWebResourceError: (WebResourceError error) {
              Navigator.pushAndRemoveUntil(
                context,
                MaterialPageRoute(builder: (context) => const ErrorPage()),
                (Route<dynamic> route) => false,
              );
            },
            onProgress: (int progress) {
              const CircularProgressIndicator();
            },
            navigationDelegate: (NavigationRequest request) {
              if (request.url.startsWith(url)) {
                return NavigationDecision.navigate;
              } else {
                return NavigationDecision.prevent;
              }
            },
            zoomEnabled: false,
            onPageStarted: (String url) {},
            onPageFinished: (String url) {},
            gestureNavigationEnabled: true,
            geolocationEnabled: true,
          );
        }),
      ),
    );
  }

  launchURL(String url) async {
    if (await canLaunch(url)) {
      await launch(url);
    } else {
      throw 'Could not launch $url';
    }
  }
}
