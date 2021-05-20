var FormStuff = {

    init: function () {
        // kick it off once, in case the radio is already checked when the page loads
        this.applyConditionalRequired();
        this.bindUIActions();
    },

    bindUIActions: function () {
        // when a radio or checkbox changes value, click or otherwise
        $("input[type='radio'], input[type='checkbox']").on("change", this
            .applyConditionalRequired);
    },

    applyConditionalRequired: function () {
        // find each input that may be hidden or not
        $(".require-if-active").each(function () {
            var el = $(this);
            // find the pairing radio or checkbox
            if ($(el.data("require-pair")).is(":checked")) {
                // if its checked, the field should be required
                el.prop("required", true);
            } else {
                // otherwise it should not
                el.prop("required", false);
            }
        });
    }

};

        var textAreaInput = ()=>{
            return(
                <div class="reveal-if-active">
                <label for="textAreaInput">What do you want this section to say?</label>
                <textarea name="textAreaInput" class="require-if-active" rows="10" cols="50"
                    data-require-pair="#choice-textAreaInput" ></textarea>
            </div>
            )
        }
        var textInput = ()=>{
            return(
                <div class="reveal-if-active">
                <label for="textAreaInput">What do you want this section to say?</label>
                <textarea name="textAreaInput" class="require-if-active" rows="10" cols="50"
                    data-require-pair="#choice-textAreaInput" ></textarea>
            </div>
            )
        }
        var textInputLabel = ()=>{
            return(
                <div class="reveal-if-active">
                <label for="textInputLabel">What is the label for your text iput?</label>
                <input type="text" id="labelInfo" name="labelInfo" value="labelinfo" ><br>
            </div>
            )
        }

FormStuff.init();
