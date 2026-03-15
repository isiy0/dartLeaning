String twoFer([String? knownName]) {
  // Replace the throw call and put your code here
  String? name = "you";
  if (knownName != null && knownName.isNotEmpty) {
    name = knownName;
  }
  String response = "One for ${name}, one for me.";
  return response;
}
