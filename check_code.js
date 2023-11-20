const buildNote = (...args) => {
  const ans = [];
  let take = true;
  for (const arg of args) {
    if (take && typeof arg === "string")
      ans.push(arg);
    take = arg === true;
  }
  return ans.join("\n");
};
const nlpExtractHandler = (prefix) => ({
  get(target, prop) {
    var _a, _b, _c, _d, _e, _f, _g, _h, _i;
    const [crit, type] = ((_a = `${prefix}${prop}`.match(/(.+)(Eval|Slots|Decision|SlotValues|Intents)$/)) != null ? _a : []).slice(1);
    switch (type) {
      case "Eval":
        return ((_b = target[crit]) == null ? void 0 : _b.evaluate) === "yes";
      case "Decision":
        return (_c = target[crit]) == null ? void 0 : _c.decision;
      case "Slots":
        return new Proxy((_e = (_d = target[crit]) == null ? void 0 : _d.slots) != null ? _e : {}, { get: (slots, key) => key in slots });
      case "SlotValues":
        return new Proxy((_g = (_f = target[crit]) == null ? void 0 : _f.slots) != null ? _g : {}, { get: (slots, key) => {
          var _a2, _b2;
          return (_b2 = (_a2 = slots[key]) == null ? void 0 : _a2.flatMap((slot) => slot.value)) != null ? _b2 : [];
        } });
      case "Intents":
        return new Proxy((_i = (_h = target[crit]) == null ? void 0 : _h.position) != null ? _i : [], { get: (positions, key) => positions.flatMap((p) => p.intents).includes(key) });
    }
    return void 0;
  }
});
const nlp = (input, prefix = "") => new Proxy(input.tempData.nlpResponse, nlpExtractHandler(prefix));
const calc = async ({ input }) => {
  var _a, _b, _c;
  const nameFromMeta = (_c = (_b = (_a = input == null ? void 0 : input.metadata) == null ? void 0 : _a.public) == null ? void 0 : _b.agent_full_name) == null ? void 0 : _c.toLocaleLowerCase();
  const { greetEval, confirmCustomerEval: customerName, agentIntroduceSlotValues, agentIntroduceEval: agentName } = nlp(input);
  const ok = greetEval && agentName && customerName;
  return {
    ok,
    result: ok ? 'Yes' : 'No',
    note: buildNote(
      !greetEval,
      "Không chào hỏi",
      !agentName,
      "Không giới thiệu tên nhân viên",
      !customerName,
      "Không xác nhận KH"
    ),
    details: `nameFromMeta: ${nameFromMeta}, nameEntities: ${agentIntroduceSlotValues.agent_name.join(",")}`
  };
};
if (typeof $input !== "undefined") {
  return calc($input.first().json.body);
}