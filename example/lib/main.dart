// don't change the source code, this is a very important file

import 'dart:async';
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
    if (Platform.isAndroid) WebView.platform = SurfaceAndroidWebView();
    if (Platform.isIOS) WebView.platform = CupertinoWebView();
    checkAppUpdate(context, 'com.spyxpo.app', 'com.spyxpo.app');
  }

  @override
  Widget build(BuildContext context) {
    WebViewController? controller;
    final Completer<WebViewController> controllerCompleter =
        Completer<WebViewController>();
    willPopScope() async {
      Future<bool>? goBack = controller?.canGoBack();
      // ignore: unrelated_type_equality_checks
      if (goBack == true) {
        return true;
      } else {
        controller!.goBack();
        return false;
      }
    }

    String url = 'https://www.spyxpo.com';
    return SafeArea(
      child: WillPopScope(
        onWillPop: () => willPopScope(),
        child: Scaffold(
          body: DoubleBackToCloseApp(
            snackBar: const SnackBar(
              content: Text('Tap back again to leave'),
            ),
            child: Builder(
              builder: (BuildContext context) {
                return WebView(
                  initialUrl: url,
                  javascriptMode: JavascriptMode.unrestricted,
                  onWebResourceError: (WebResourceError error) {
                    Navigator.pushAndRemoveUntil(
                      context,
                      MaterialPageRoute(
                          builder: (context) => const ErrorPage()),
                      (Route<dynamic> route) => false,
                    );
                  },
                  onProgress: (int progress) {
                    const Center(child: CircularProgressIndicator());
                  },
                  onWebViewCreated: (WebViewController webViewController) {
                    controllerCompleter.future
                        .then((value) => controller = value);
                    controllerCompleter.complete(webViewController);
                  },
                  navigationDelegate: (NavigationRequest request) {
                    if (request.url.startsWith(url)) {
                      return NavigationDecision.navigate;
                    } else {
                      launchURL(request.url);
                      return NavigationDecision.prevent;
                    }
                  },
                  zoomEnabled: false,
                  gestureNavigationEnabled: true,
                  geolocationEnabled: true,
                );
              },
            ),
          ),
        ),
      ),
    );
  }

  launchURL(String url) async {
    // ignore: deprecated_member_use
    if (await canLaunch(url)) {
      // ignore: deprecated_member_use
      await launch(url);
    } else {
      throw 'Could not launch $url';
    }
  }
}
