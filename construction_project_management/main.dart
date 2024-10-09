import 'package:flutter/material.dart';
import 'loading_page.dart';  // Import the loading page
import 'dashboard_page.dart';  // Import the dashboard page

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Preferred Plan',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: LoadingToDashboard(),  // Start with the loading page
    );
  }
}

class LoadingToDashboard extends StatefulWidget {
  @override
  _LoadingToDashboardState createState() => _LoadingToDashboardState();
}

class _LoadingToDashboardState extends State<LoadingToDashboard> {
  @override
  void initState() {
    super.initState();
    // Simulate a loading delay of 3 seconds
    Future.delayed(Duration(seconds: 3), () {
      // Navigate to the dashboard after the delay
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => DashboardPage()),
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return LoadingPage();  // Show the loading page while waiting
  }
}
