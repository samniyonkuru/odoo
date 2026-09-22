{ pkgs }:

pkgs.mkShell {
  packages = with pkgs; [
    zsh
    python3
    postgresql
    postgresql.pg_config
    openldap
    cyrus_sasl
    pyright
  ];

  LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc.lib
  ];

  shellHook = ''
    export DEVENV_NAME="odoo"

    if [ -z "$ZSH_VERSION" ]; then
      exec zsh
    fi
  '';
}
