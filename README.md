### Versioner
Version reader/writer for popular package managers


#### Installation

    pip install git+https://stash.veritas.com/scm/surf/versioner.git


#### Usage
- Run below command from project root

        > versioner read npm  # projects based on npm
        0.0.1

        > versioner read dep  # golang projects
        0.1.1

- Read version from custom file

        > versioner read npm --file /root/app/version.yaml --version-hierarchy myapp,version
        0.0.2

        version.yaml
        ---
        myapp:
          version: 0.0.2


#### Development

    git clone https://stash.veritas.com/scm/surf/versioner.git
    cd versioner
    pip install -e .
