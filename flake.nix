{
    description = "example dev env";

    inputs = {
        nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    };

    outputs = { self, nixpkgs }: 
        let
        pkgs = nixpkgs.legacyPackages."x86_64-linux";
    in
    {
# importing package example
# packages."x86_64-linux".default = 
#   pkgs.callPackage (import ./default.nix) {};

        devShells."x86_64-linux".default = pkgs.mkShell {

            packages = with pkgs; [
                /* put packages here */ 
                python3
                python3Packages.requests
                python3Packages.python-pptx
                python3Packages.python-docx
                python3Packages.pymupdf
                python3Packages.pandas
                python3Packages.watchdog
            ];

            shellHook = ''
                export SHELL=$(which fish)
                exec $SHELL
                '';
        };
    };
}
