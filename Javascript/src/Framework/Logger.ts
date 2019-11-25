export class Logger {
    public static Instance = new Logger();
    // tslint:disable-next-line: no-empty
    constructor() { }
    public LogInformational(text: string): void {
        // tslint:disable-next-line: no-console
        console.log(`%c${text}`, "color:#cce5ff;");
    }
    public LogError(text: string): void {
        // tslint:disable-next-line: no-console
        console.log(`%c${text}`, "color:red");
    }
}