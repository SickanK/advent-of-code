use proc_macro::TokenStream;
use quote::quote;
use syn;
use syn::Lit::Int;
use syn::NestedMeta;

#[proc_macro_attribute]
pub fn aoc(attrs: TokenStream, item: TokenStream) -> TokenStream {
    let input = syn::parse_macro_input!(item as syn::ItemFn);
    let parsed_attrs = syn::parse_macro_input!(attrs as syn::AttributeArgs);

    let mut args: Vec<usize> = Vec::with_capacity(2);

    for i in 0..2 {
        match &parsed_attrs[i] {
            NestedMeta::Meta(_) => panic!("Insert valid integers (year, day)"),
            NestedMeta::Lit(lit) => {
                if let Int(arg_int) = lit.to_owned() {
                    args.push(
                        arg_int
                            .base10_parse()
                            .unwrap_or_else(|_| panic!("Insert valid integers (year, day)")),
                    );
                }
            }
        };
    }

    let name = &input.sig.ident;
    let block = &input.block;
    let output = &input.sig.output;
    let inputs = &input.sig.inputs;
    let mut inputs_iter = inputs.iter();
    let input_name = inputs_iter.next().expect("msg");

    let year: u16 = args[0] as u16;
    let day: u8 = args[1] as u8;

    TokenStream::from(quote! {
        pub fn #name() #output {
            let #input_name = raoc::get_puzzle_input(#year, #day).ok().unwrap();

            #block
        }
    })
}
