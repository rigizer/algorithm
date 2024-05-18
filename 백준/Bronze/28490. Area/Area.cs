namespace Solution {
  class Program {
    static void Main(string[] args) {
      var n = int.Parse(Console.ReadLine()!);
      int maxArea = 0;
      for (int i = 0; i < n; i++) {
        var input = Console.ReadLine()!.Split(' ');
        var h = int.Parse(input[0]);
        var w = int.Parse(input[1]);
        maxArea = Math.Max(maxArea, h * w);
      }
      Console.WriteLine(maxArea);
    }
  }
}