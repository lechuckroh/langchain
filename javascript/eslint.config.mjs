import globals from "globals";
import pluginJs from "@eslint/js";
import tseslint from "typescript-eslint";

/** @type {import('eslint').Linter.Config[]} */
export default [
    {
        ignores: [
            "node_modules/*",
            "apps/*/node_modules/*",
            "apps/*/dist/*",
            "**/*.js",
        ],
    },
    { files: ["**/*.ts"] },
    { languageOptions: { globals: globals.node } },
    pluginJs.configs.recommended,
    ...tseslint.configs.recommended,
];
