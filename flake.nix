{
  description = "Pygame Animation Development Environment";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let 
      system = "x86_64-linux"; # Passe dies an dein System an, z. B. aarch64-linux
      pkgs = import nixpkgs { inherit system; };
    in {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = [
          pkgs.python3
          pkgs.python3Packages.pygame
          pkgs.python3Packages.imageio
          pkgs.python3Packages.imageio-ffmpeg # Hier wird das MP4-Backend hinzugefügt
          pkgs.ffmpeg # Stellt sicher, dass FFMPEG verfügbar ist
        ];
        shellHook = ''
          echo "Entwicklungsumgebung für Pygame gestartet!"
        '';
      };
    };
}
