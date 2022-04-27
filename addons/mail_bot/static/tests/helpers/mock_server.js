/** @odoo-module **/

import MockServer from 'web.MockServer';

MockServer.include({
    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    async _performRpc(route, args) {
        if (args.model === 'mail.channel' && args.method === 'init_odoobot') {
            return this._mockMailChannelInitmidrarsolutionsBot();
        }
        return this._super(...arguments);
    },

    //--------------------------------------------------------------------------
    // Private Mocked Methods
    //--------------------------------------------------------------------------

    /**
     * Simulates `init_odoobot` on `mail.channel`.
     *
     * @private
     */
    _mockMailChannelInitmidrarsolutionsBot() {
        // TODO implement this mock task-2300480
        // and improve test "midrarsolutionsBot initialized after 2 minutes"
    },
});
