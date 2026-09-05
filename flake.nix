{
  description = "Prog-env";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in {
      devShells.${system} = {
        frontend = import ./frontend/shell.nix { inherit pkgs; };
        backend  = import ./backend/shell.nix { inherit pkgs; };
        default = import ./shell.nix { inherit pkgs; };
      };
    };
}
