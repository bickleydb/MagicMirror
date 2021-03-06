
export class KeyValueDictionary {

    private backing: { [key: string]: any  };

    constructor() {
        this.backing = {};
    }

    public GetValue(key: string): any {
        if (!this.backing[key]) {
            return null;
        }
        return this.backing[key];
    }

    public Add(key: string, value: any): void {
        if (this.backing[key]) {
            delete this.backing[key];
        }
        this.backing[key] = value;
    }
}
