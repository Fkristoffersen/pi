const path=require("path");delete process.env.ELECTRON_RUN_AS_NODE,process.env.VSCODE_DEV?(process.env.VSCODE_INJECT_NODE_MODULE_LOOKUP_PATH=process.env.VSCODE_INJECT_NODE_MODULE_LOOKUP_PATH||path.join(__dirname,"..","remote","node_modules"),require("./bootstrap-node").injectNodeModuleLookupPath(process.env.VSCODE_INJECT_NODE_MODULE_LOOKUP_PATH)):delete process.env.VSCODE_INJECT_NODE_MODULE_LOOKUP_PATH,require("./bootstrap-amd").load("vs/server/node/server.cli");

//# sourceMappingURL=https://ticino.blob.core.windows.net/sourcemaps/4af164ea3a06f701fe3e89a2bcbb421d2026b68f/core/server-cli.js.map
