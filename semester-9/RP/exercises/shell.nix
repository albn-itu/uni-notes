with (import <nixpkgs> {});
let
  python-packages = ps:
    with ps; [
      numpy
    ];
in
  mkShellNoCC {
    packages = with pkgs; [
      ((python3.withPackages python-packages).override (args: {ignoreCollisions = true;}))
    ];
  }
