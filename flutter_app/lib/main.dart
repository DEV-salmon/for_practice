import 'package:flutter/material.dart';

void main() {
  runApp(FragranceApp());
}

class FragranceApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Niche Perfume Platform',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: FragranceHomePage(),
    );
  }
}

class FragranceHomePage extends StatefulWidget {
  @override
  _FragranceHomePageState createState() => _FragranceHomePageState();
}

class _FragranceHomePageState extends State<FragranceHomePage> {
  final List<String> baseNotes = ['Musk', 'Amber', 'Vanilla'];
  final List<String> middleNotes = ['Rose', 'Jasmine', 'Lavender'];
  final List<String> topNotes = ['Bergamot', 'Lemon', 'Orange'];

  String? selectedBase;
  String? selectedMiddle;
  String? selectedTop;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Create Your Scent'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Select Base Note'),
            DropdownButton<String>(
              value: selectedBase,
              onChanged: (value) => setState(() => selectedBase = value),
              items: baseNotes.map((note) => DropdownMenuItem(value: note, child: Text(note))).toList(),
            ),
            SizedBox(height: 16),
            Text('Select Middle Note'),
            DropdownButton<String>(
              value: selectedMiddle,
              onChanged: (value) => setState(() => selectedMiddle = value),
              items: middleNotes.map((note) => DropdownMenuItem(value: note, child: Text(note))).toList(),
            ),
            SizedBox(height: 16),
            Text('Select Top Note'),
            DropdownButton<String>(
              value: selectedTop,
              onChanged: (value) => setState(() => selectedTop = value),
              items: topNotes.map((note) => DropdownMenuItem(value: note, child: Text(note))).toList(),
            ),
            SizedBox(height: 24),
            ElevatedButton(
              onPressed: (selectedBase != null && selectedMiddle != null && selectedTop != null)
                  ? () {
                      final scent = 'Base: $selectedBase, Middle: $selectedMiddle, Top: $selectedTop';
                      showDialog(
                        context: context,
                        builder: (_) => AlertDialog(
                          title: Text('Your Scent'),
                          content: Text(scent),
                        ),
                      );
                    }
                  : null,
              child: Text('Preview'),
            ),
          ],
        ),
      ),
    );
  }
}
